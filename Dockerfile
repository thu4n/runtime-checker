FROM python:3.10-bookworm

COPY connect.py .

RUN pip install "python-socketio[asyncio]" aiohttp

ENTRYPOINT ["python", "connect.py"]