#### Downloading a single video
docker run -it --rm -e url=<URL_OF_VIDEO> -e quality=half -v <DOWNLOAD_LOCATION>:/opt/download bytenerdalpha/black_ring_downloader:v0.0.1

eg: docker run -it --rm -e url=https://www.p***b.com/view_video.php?viewkey=1321312323 -e quality=half -v /tmp/test:/opt/download bytenerdalpha/black_ring_downloader:v0.0.1
