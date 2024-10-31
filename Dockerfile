# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the codebase to the working directory
COPY . .

EXPOSE 8080

# Define the command to run the app
CMD ["python", "app.py"]
