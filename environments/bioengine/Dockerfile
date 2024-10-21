FROM ghcr.io/amun-ai/hypha:0.20.35.post2
COPY . /app
USER root
RUN pip install -r /app/requirements.txt
RUN pip install /app
USER hypha