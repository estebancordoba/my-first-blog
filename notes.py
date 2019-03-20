python -m venv myvenv
myvenv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt -> Django~=2.1.7
django-admin.exe startproject mysite .

America/Bogota

python manage.py migrate
python manage.py runserver

python manage.py startapp blog
python manage.py makemigrations blog
python manage.py migrate blog

python manage.py createsuperuser

git init