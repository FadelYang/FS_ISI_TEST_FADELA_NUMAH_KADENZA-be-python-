# Use official Python image
FROM python:3.10.12

# Set working directory inside container
WORKDIR /app

# Copy requirements and install deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your FastAPI app
COPY . .

# Expose port FastAPI will run on
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
