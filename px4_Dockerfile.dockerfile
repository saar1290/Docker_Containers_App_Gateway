FROM ubuntu:20.04

# Installing necessary prerequisite packages and making a directory for the app.
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y && apt install wget git lsb-release sudo gnupg2 -y 

# Clone the project to the root directory, and install the PX4 app dependencies.
RUN git clone https://github.com/PX4/PX4-Autopilot.git --recursive && \
bash PX4-Autopilot/Tools/setup/ubuntu.sh && \
rm -rf /var/lib/apt/lists/*

# Make a proper directory for the run scripts and copy them to it, and change position to scripts directory. 
RUN mkdir /PX4-Autopilot/Scripts
COPY run-airsim-sitl.sh /PX4-Autopilot/Scripts
COPY build_px4_none_iris.sh /PX4-Autopilot/

# Run the build script
WORKDIR /PX4-Autopilot
RUN bash /PX4-Autopilot/build_px4_none_iris.sh

# finally trigger the run script when a container is created.
WORKDIR /PX4-Autopilot/Scripts
CMD ./run-airsim-sitl.sh