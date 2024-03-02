#### Downloading a single video
docker run -it --rm -e url=<URL_OF_VIDEO> -e quality=half -v <DOWNLOAD_LOCATION>:/opt/download bytenerdalpha/black_ring_downloader:v0.0.1

eg: docker run -it --rm -e url=https://www.p***b.com/view_video.php?viewkey=1321312323 -e quality=half -v /tmp/test:/opt/download bytenerdalpha/black_ring_downloader:v0.0.1


#### Running a monitoring service
This will allow you to run a container in monitor mode. It monitors for a text file and downloads any phub url's that are added to it.
docker run -it --rm -e quality=half -v <FILE_LOCATION_WITH_URLS>:/tmp/download.txt -v <DOWNLOAD_LOCATION>:/opt/download bytenerdalpha/black_ring_monitor:v0.0.1

eg: docker run -it --rm -e quality=half -v /home/random/myinput.txt:/tmp/download.txt -v /tmp/test:/opt/download bytenerdalpha/black_ring_monitor:v0.0.1

#### Running downloads through a vpn
The included docker-compose file allows you to run a VPN and run downloads through the VPN network alone. This allows you to configure a
VPN network that only the downloading container uses.

The included example config is for surfshark vpn:
* copy the env.template file to a .env file
* Update the values in .env file based on guide here: https://code.mendhak.com/run-docker-through-vpn-container/
* Run the vpn: docker-compose up -d surf
* Run the monitor service: docker-compose up black_ring


#### Credits
Based on: https://github.com/EchterAlsFake/PHUB (Salute to the maintainer)