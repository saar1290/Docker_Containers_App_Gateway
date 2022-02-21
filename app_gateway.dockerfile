FROM ubuntu:20.04

# Installing necessary prerequisite packages and making a directory for the app.
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y && \
apt install python3-pip python3 curl -y && mkdir /app && rm -rf /var/lib/apt/lists/*

# Installing necessary python libraries 
RUN pip3 install docker fastapi uvicorn

# Copy the app code to the root directory
COPY main.py /app

# Change position to the app directory
WORKDIR /app

# Finally trigger the main.py when a container is created
CMD python3 main.py