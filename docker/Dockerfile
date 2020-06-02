FROM django:latest
RUN apt-get update -y && apt-get install -y git-core
RUN pip install -U pylint --user
RUN pip install pip --upgrade
RUN pip install django --upgrade
RUN pip install django-ckeditor
RUN pip install pymysql
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install openpyxl
# CMD ["python", "/app/book/manage.py", "runserver","0.0.0.0:8000"]
