# Use Python 3.10.9-alpine3.16 as the base image
FROM python:3.10.9-alpine3.16

# Copy the script to the container
COPY domains_check.py /app/domains_check.py

# Set the working directory to /app
WORKDIR /app

# Run the script every minute using cron
RUN echo "0 */6 * * * python /app/domains_check.py" >> /var/spool/cron/crontabs/root \
    && pip install requests

# Set the timezone to Asia/Shanghai
ENV TZ=Asia/Shanghai

# Start the cron service
CMD ["crond", "-f", "-l", "8"]