# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY app1.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app1.py"]
