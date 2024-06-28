FROM docker.arvancloud.ir/python:3.11.1-slim
# Set working directory to /usr/src/app
WORKDIR /usr/src/app
# Copy the contents of the current local directory into the container's working directory
ADD . /usr/src/app
# Run a command
CMD ["python", "hello.py"]