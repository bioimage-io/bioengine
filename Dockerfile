FROM ghcr.io/amun-ai/hypha:0.15.51

COPY . /app
RUN pip install -r /app/requirements.txt
RUN pip install /app

