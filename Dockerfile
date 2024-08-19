FROM python:3.12-slim

ARG DATABASE_URL
ARG JWT_SECRET

ENV DATABASE_URL=${DATABASE_URL}
ENV JWT_SECRET=${JWT_SECRET}


ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV DEBUG_MODE=False


WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

EXPOSE 5000

# Comando para iniciar o aplicativo
# CMD ["flask", "run", "--host=0.0.0.0"]
# CMD [ "python", "app.py" ]
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
