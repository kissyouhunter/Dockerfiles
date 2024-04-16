# Stage 1: Building the application
FROM node:18-alpine as builder

# Set the working directory
WORKDIR /app

# Copy package.json and pnpm-lock.yaml files
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN npm install -g pnpm && pnpm install

# Copy the project files
COPY . .

# Build the application
RUN pnpm run build

# Stage 2: Running the application
FROM nginx:alpine

# Copy the Nginx configuration file
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy the files built in stage 1
COPY --from=builder /app/dist /usr/share/nginx/html
