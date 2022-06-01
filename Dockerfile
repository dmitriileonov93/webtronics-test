FROM python:3.7-slim
COPY ./ /app
RUN python3 -m pip install --upgrade pip && \
    pip install -r /app/requirements.txt
WORKDIR /app/social_network/
CMD python3 manage.py migrate && \
    python3 manage.py loaddata data_dump.json && \
    python3 manage.py collectstatic --noinput && \
    gunicorn social_network.wsgi:application --bind 0:8000