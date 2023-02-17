## Setup Instructions:
1. Make sure you have `python` and `node.js` installed.
2. Clone the repo:
    ```
    git clone https://github.com/utchchhwas/GoodReads.git
    cd GoodReads
    ```
3. Setup and activate `python` virtual environment:
    ```
    python -m venv venv
    venv/Scripts/Activate.ps1
    ```
4. Install dependencies and run server:
    ```
    ./setup.ps1     # powershell
    ```
    ```
    ./setup.sh      # bash
    ```

## Admin Credentials:
```
username: admin
password: admin
```

## API Endpoints
 - http://127.0.0.1:8000/ [Homepage]
 - http://127.0.0.1:8000/admin/ [Admin Panel]
 - http://127.0.0.1:8000/api/authors/ [Get all authors.]
 - http://127.0.0.1:8000/api/authors/1/ [Get a specific author.]
 - http://127.0.0.1:8000/api/publishers/ [Get all publishers.]
 - http://127.0.0.1:8000/api/book_catagories/ [Get all catagories.]
 - http://127.0.0.1:8000/api/child_book_catagories/1/ [Get all the childs of a catagory.]
 - http://127.0.0.1:8000/api/books/ [Get all books.]
 - http://127.0.0.1:8000/api/books/1/ [Get a specific book.]
 - http://127.0.0.1:8000/api/search/?keyword=concrete [Search books.]
