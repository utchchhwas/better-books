pip install -r requirements.txt
cd frontend
npm install && npm run build
cd ..
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
