#!/bin/bash

# This is a shell script for building image for the server 

# Set the necessary environment variables
# TODO: Add any required environment variables here

# Change to the project directory
# cd server

# TODO: Add your build commands here
nerdctl build -t my-prometheus-image .
nerdctl save -o my-prometheus-image.tar my-prometheus-image:latest
microk8s ctr image import my-prometheus-image.tar

# Print a success message
echo "Build completed successfully!"