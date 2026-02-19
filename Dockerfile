# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the necessary libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy your python script into the container
# Ensure your script is named 'main.py' or change the name below
COPY main.py .

# Run the bot
CMD ["python", "main.py"]