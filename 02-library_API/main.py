from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Library Management API")


# book_information
class Book(BaseModel):
    title: str
    author: str
    published_year: int
    available: bool = True


# save_data
books = {}
next_id = 1


# collect_All_book
@app.get("/books")
def get_books():
    return list(books.values())


# pick_one_bookById
@app.get("/books/{book_id}")
def get_book(book_id: int):
  book = books.get(book_id)
  if book is None:
    raise HTTPException(
      status_code=404,
      detail="Book not found"
    )
  return book


# Add_new_book
@app.post("/books", status_code=201)
def create_book(book: Book):
    global next_id

    new_book = {
        "id": next_id,
        **book.model_dump()
    }

    books[next_id]=(new_book)
    next_id += 1

    return new_book


# edite_book
class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    published_year: int | None = None
    available: bool | None = None


# edit2_book
@app.patch("/books/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):
    book = books.get(book_id)
    if book is None:
      raise HTTPException(
        status_code=404,
        detail="Book not found"
      )

    update_data = book_update.model_dump(
      exclude_unset=True
    )

    for key, value in update_data.items():
      if value is None:
        raise HTTPException(
          status_code=422,
          detail=f"{key} cannot be null"
        )

    book.update(update_data)

    return book




# delete_book
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
  if book_id not in books:
    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
  del books[book_id]
  return None