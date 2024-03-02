# Use an official Python runtime as a parent image
FROM python:latest

ENV url phub_url
ENV quality medium

#RUN pip install --upgrade git+https://github.com/EchterAlsFake/PHUB.git
RUN pip install --upgrade phub click
RUN mkdir -p /opt/download

# Run app.py when the container launches
CMD ["sh", "-c", "python -m phub download ${url} --quality ${quality} --output /opt/download"]