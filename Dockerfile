# Use an official Python runtime as a parent image
FROM python:latest

ENV quality half

RUN pip install --upgrade phub click watchdog
RUN mkdir -p /opt/download

ADD monitor.py /opt/

# Run app.py when the container launches
CMD ["sh", "-c", "python /opt/monitor.py"]