# lab6
Реалізувати REST-сервіс (операції GET/POST/PUT/DELETE) для одного з класу з лабораторної роботи 3 з використанням засобів мови Python:
Flask
Python 3.x
2. Реалізувати збереження об'єкту класу з лабораторної роботи 3 в базі даних з використанням наступного технологічного стеку 
SQLAlchemy-1.1.15
MySQL-5.7 / MySQL-8.0 (в залежності від того, яку базу даних було обрано в 8-й роботі)

Інструкція по Flask доступн за посиланням: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

PIP installation: https://pip.pypa.io/en/latest/installing/

Flask: https://ru.wikibooks.org/wiki/Flask


Перед виконанням роботи слід пересвідчитись що на вашому комп’ютері встановлено Python 3 та налаштовані змінні середовища, як описано в першій презентації по мові Python

1. Для створення віртуального середовища необхідно запустити команду: 
python3 -m venv venv (Unix/Linux/Mac) or py instead python for Windows

2. Встановлення Pipenv
Pipenv - це система управління залежностями для мови Python. На відміну від мови Java системи управління maven, в мові Python використовується концепція віртуальних середовищ. Віртуальне середовище - це фактично налаштована робоча машина під потреби конкретного проекту. Але є одне але: Pipenv дозволить розробляти проекти, які вимагають різні версії Python. Для використання різних версій мови Java застосовуються плагіни (maven-compiler-plugin) та змінні середовища. 
Встановлення:
pip install --user pipenv
Або pip3 install --user pipenv 

3. Встановлення virtualenv
Virtualenv - це інструмент для створення ізольованих середовищ Python. virtualenv створює папку, яка містить всі необхідні виконувані файли, щоб використовувати пакети, необхідні для проекту на мові Python.
pip install virtualenv
4. Активізуйте іваше віртуальне середовище з використанням команди: 
source my_project/bin/activate

Or venv\Scripts\activate.bat for Windows

5. Встановіть фласк виконавши команду: pip3 install flask

