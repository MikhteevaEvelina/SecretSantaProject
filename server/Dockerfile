FROM node:16.13.2

LABEL version="1.0"
LABEL description="server part of Secret Santa"

# Make folder to put our files in
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/server
# Set working directory so that all subsequent command runs in this folder
WORKDIR /usr/src/app/server
# Copy package json and install dependencies
COPY package*.json ./
RUN npm install
# Copy our app
COPY . .
# Expose port to access server
EXPOSE 5000
# Command to run our app
CMD ["npm", "run", "dev"]
