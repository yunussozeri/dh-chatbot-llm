# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 8001

# Run the Flask app when the container starts
CMD ["python", "-m", "llm_query_engine.llm_query_engine_api"]
