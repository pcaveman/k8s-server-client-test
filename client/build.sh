#!/bin/bash

# This is a shell script for building image for the client 

# Set the necessary environment variables
# TODO: Add any required environment variables here

# Change to the project directory
# cd client

# TODO: Add your build commands here
nerdctl build -t my-client-image .
nerdctl save -o my-client-image.tar my-client-image:latest
microk8s ctr image import my-client-image.tar

# Print a success message
echo "Build completed successfully!"