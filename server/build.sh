#!/bin/bash

# This is a shell script for building image for the server 

# Set the necessary environment variables
# TODO: Add any required environment variables here

# Change to the project directory
# cd server

# TODO: Add your build commands here
nerdctl build -t my-server-image .
nerdctl save -o my-server-image.tar my-server-image:latest
microk8s ctr image import my-server-image.tar

# Print a success message
echo "Build completed successfully!"