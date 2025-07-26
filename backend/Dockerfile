FROM python:3.10-slim

# Set working directory
WORKDIR /app 

# Install system dependencies
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# after copying the repo:
#RUN rm -f /app/tests/test_auth.py

# Expose the port the app runs on
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]