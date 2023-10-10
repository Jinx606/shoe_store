# Use the official Python image as the base image
FROM python:3.9.6

# Set the working directory inside the container
WORKDIR /app

# Copy your Python code and inventory.txt into the container
COPY inventory.py inventory.txt /app/

# Install any Python dependencies (if needed)
RUN pip install tabulate

# Command to run your Python script
CMD [ "python", "inventory.py" ]
