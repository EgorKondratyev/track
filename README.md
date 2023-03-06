Устанавливаем пакеты:
```python
pip install Django
pip install django-allauth
pip install django-simple-captcha
```
Выполним миграцию:
```
Windows: venv\Scirpts\activate | Linux: venv/bin/activate
cd .../track/
python manage.py migrate
```