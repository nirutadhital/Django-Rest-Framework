FROM python:3.12

WORKDIR /backend

COPY backend/ /backend/

COPY requirements.txt /backend/

RUN pip install --no-cache-dir -r requirements.txt
#requirements.txt

EXPOSE 8000
CMD [ "python", "manage.py", "runserver" ]




