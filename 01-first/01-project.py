import requests , random , time , csv 
from typing import List, Dict, Callable, Optional

base_url = 'https://openlibrary.org/search.json'

subjects = [
  'science_fiction',
  'fantasy',
  'history',
  'philosophy',
  'programming',
  'romance',
  'mystery',
  'biography',
  'poetry'
]

def fetch_random_book(count=10):
  books = []
  attempts = 0
  max_attempt = count*5

  while len(books)< count and  attempts < max_attempt:
    attempts += 1
    subject = random.choice(subjects)
    offset = random.randint(0,5000)

    params = {
      "q":f'subject:{subject}',
      "limit":10,
      "offset":offset,
      "fields": "key,title,author_name,first_publish_year,"
                      "language,number_of_pages_median,subject,"
                      "publisher,isbn,ratings_average,ratings_count"
    }

    try:
      response = requests.get(base_url,params=params,timeout=10)
      response.raise_for_status()
      data = response.json()

      for docs in data.get("docs",[]):
        if docs not in books:
          books.append(docs)
          if len(books)>= count:
            break

    except requests.RequestException as e:
      print(f'some thing is wrong: {e}')
    time.sleep(1)
  return books[:count]

def filter_books(
    books: List[Dict],
    min_year: Optional[int] = None,
    max_year: Optional[int] = None,
    min_pages: Optional[int] = None,
    max_pages: Optional[int] = None,
    language: Optional[str] = None,
    min_rating: Optional[float] = None,
    author_contains: Optional[str] = None,
    custom_filter: Optional[Callable[[Dict], bool]] = None
) -> List[Dict]:
  def matches(book: Dict) -> bool:
    # publish_year
    year = book.get("first_publish_year")
    if min_year is not None and (year is None or year < min_year):
        return False
    if max_year is not None and (year is None or year > max_year):
        return False

    # number_of_page
    pages = book.get("number_of_pages_median")
    if min_pages is not None and (pages is None or pages < min_pages):
        return False
    if max_pages is not None and (pages is None or pages > max_pages):
        return False

    # language
    if language:
        langs = book.get("language", [])
        if language not in langs:
            return False

    # rating
    rating = book.get("ratings_average")
    if min_rating is not None and (rating is None or rating < min_rating):
        return False

    # outhor
    if author_contains:
        authors = " ".join(book.get("author_name", []))
        if author_contains.lower() not in authors.lower():
            return False

    if custom_filter is not None and not custom_filter(book):
        return False

    return True
  return [b for b in books if matches(b)]
   
def save_book( books: List[Dict] , file_name:str = 'savebooks.csv'):
  if not books:
     print("ther is not any book to save")
     return
  try:
    with open(file_name,'w',encoding='utf-8-sig',newline='') as f:
      writer = csv.writer(f)
      titels = list(books[0].keys()) 
      writer.writerow([b for b in titels])
      writer.writerow([])
      for i in books:
        row = list(i.values())
        writer.writerow(row)
  except OSError as e:
    print(f'saving data was failed: {e}\ntry agane!!')



# ---------- test code ----------
  
print("🔍 finding some random book...")
random_books = fetch_random_book(count=30)
print(f"number of books : {len(random_books)}")

#filter books
filtered = filter_books(
    random_books,
    min_year=2000,
    #min_pages=100,
    #min_rating=3.5,
    language="eng"
)
print(f"number of books after filtering: {len(filtered)}")

# show result and save
#for book in filtered:
  #print(f"- {book.get('title')} ({book.get('first_publish_year')}) "
        #f"| {book.get('number_of_pages_median')} page")

save_book(filtered, "savebooks.csv")

