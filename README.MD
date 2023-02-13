## Setup Instructions:
1. Make sure you have `python` and `npm` installed.
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
4. Install dependencies:
    ```
    pip install -r requirements.txt
    cd frontend && npm install
    ```
5. Run `react` server:
    ```
    npm start
    ```
6. Run `django` server:
    ```
    cd ../backend
    python manage.py runserver 
    ```
