FROM python:3.9

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip wheel setuptools
RUN pip install -r requirements.txt

# Copy application code
COPY . /app/

# Expose the port on which the app will run
EXPOSE 8008

# Start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
