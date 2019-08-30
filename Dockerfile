FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN adduser pyuser

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x main.py

RUN chown -R pyuser:pyuser /app
USER pyuser


EXPOSE 5000
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000", "-w", "4"]