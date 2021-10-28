docker run -itd \
    --name library-web \
    -w /code \
    -v /opt/clients_projects/library-test-project:/code \
    -p 8344:8000 \
    python:3.10 \
    /bin/bash \
    -c "pip install --upgrade pip && pip install -r requirements.txt && src/manage.py migrate && src/manage.py runserver 0.0.0.0:8000"
