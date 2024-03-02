#### Downloading a single video
docker run -it --rm -e url=<URL_OF_VIDEO> -e quality=half -v <DOWNLOAD_LOCATION>:/opt/download bytenerdalpha/black_ring_downloader:v0.0.1

eg: docker run -it --rm -e url=https://www.p***b.com/view_video.php?viewkey=1321312323 -e quality=half -v /tmp/test:/opt/download bytenerdalpha/black_ring_downloader:v0.0.1


#### Running a monitoring service
This will allow you to run a container in monitor mode. It monitors for a text file and downloads any phub url's that are added to it.




#### Credits
Based on: https://github.com/EchterAlsFake/PHUB (Salute to the maintainer)