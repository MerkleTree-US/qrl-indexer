# Dockerfile
FROM python:3.8

# Update system packages
RUN apt-get update && apt-get upgrade -y

# Install git
RUN apt-get install -y git

# Set the working directory
WORKDIR /app

# Clone the repository with the proto file
RUN git clone https://github.com/theQRL/QRL.git ./qrl

# Clone the Google APIs
RUN git clone https://github.com/googleapis/googleapis.git ./googleapis

# Copy the current directory contents into the container
COPY . .

# Install the necessary Python packages
RUN pip install -r requirements.txt

# Create the proto directory
RUN mkdir -p ./qrl/proto

# Generate Python gRPC code from the proto file
RUN python -m grpc_tools.protoc -I./qrl/src/qrl/protos -I./googleapis --python_out=./qrl/proto --grpc_python_out=./qrl/proto ./qrl/src/qrl/protos/qrl.proto

# Run the Python script
CMD ["python", "main.py"]