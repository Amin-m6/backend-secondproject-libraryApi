# 📚 Random Book Finder

A Python-based project that uses the Open Library API to fetch random books,
filter them based on different criteria, and save the filtered results into
a CSV file.

## 📌 About The Project

This project is designed to practice working with public APIs in Python.

The application connects to the Open Library API and retrieves information
about books from different subjects such as:

- Science Fiction
- Fantasy
- History
- Philosophy
- Programming
- Romance
- Mystery
- Biography
- Poetry

The program randomly selects subjects and pages of results, retrieves book
information, removes duplicate books, and then allows the collected books
to be filtered using different criteria.

The final filtered results can be exported to a CSV file.

## 🚀 Features

- Fetch random books from the Open Library API
- Select books from different subjects
- Avoid duplicate books
- Filter books by publication year
- Filter books by number of pages
- Filter books by language
- Filter books by rating
- Search for books by author name
- Support custom filtering functions
- Save book information as a CSV file
- Handle API request errors
- Set a timeout for API requests

## 🛠️ Technologies

- Python 3
- Requests
- Open Library API
- CSV
- JSON
- Git
- GitHub

## 📡 API

This project uses the Open Library Search API:

Open Library:
https://openlibrary.org/

API endpoint:

https://openlibrary.org/search.json

The API is used to retrieve information such as:

- Book title
- Author
- First publication year
- Language
- Number of pages
- Subjects
- Publisher
- ISBN
- Average rating
- Number of ratings

## 📦 Requirements

Python 3.x is required to run this project.

The project also uses the `requests` library.

Install it using:

```bash
pip install requests