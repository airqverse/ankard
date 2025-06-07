# Stage 1: Build the frontend app
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm install

# Copy source files and build
COPY . .
RUN npm run build

# Stage 2: Serve with NGINX
FROM nginx:alpine

# Copy built files to nginx public directory
COPY --from=builder /app/dist /usr/share/nginx/html

# Optional: Replace default nginx config if needed
# COPY nginx.conf /etc/nginx/nginx.conf

# Inform Docker that this container will listen on port 80.
# The reason not using 433 is because this port is used internally by containers.
EXPOSE 80

# Default command (nginx will auto-start)
CMD ["nginx", "-g", "daemon off;"]
