FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080

CMD ["streamlit", "run", "frontend.py", "--server.port=8080", "--server.address=0.0.0.0",
"--browser.gatherUsageStats=false"]
