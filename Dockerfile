# ---------- Round 1 A Dockerfile ----------
FROM --platform=linux/amd64 python:3.11-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt            # wheels only

COPY . .                                                     # copy source
ENTRYPOINT ["python", "main_1a.py"]                          # batch runner
