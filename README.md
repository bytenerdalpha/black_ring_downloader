### How to Use

#### Download a Single Video

For direct video downloading, we use `black_ring_downloader`.

1. Substitute `<URL_OF_VIDEO>` with the actual video URL and `<DOWNLOAD_LOCATION>` with your chosen location.

   Example:

   ```sh
   docker run -it --rm -e url=https://www.p***b.com/view_video.php?viewkey=1321312323 -e quality=half -v /tmp/test:/opt/download bytenerdalpha/black_ring_downloader:v0.0.1
   ```

#### Run a Monitoring Service

The `black_ring_monitor` allows continuous monitoring and downloading of URLs found in a text file.

1. Provide your `<FILE_LOCATION_WITH_URLS>` and `<DOWNLOAD_LOCATION>` in the below command.

   Example:

   ```sh
   docker run -it --rm -e quality=half -v /home/random/myinput.txt:/tmp/download.txt -v /tmp/test:/opt/download bytenerdalpha/black_ring_monitor:v0.0.1
   ```

#### Run Downloads Through a VPN

With the docker-compose file and a VPN, you can ensure your downloads are done via the VPN network. The example provided here is for Surfshark VPN.

1. Copy the `env.template` file to a `.env` file.
2. Update the `.env` based on the guide [here](https://code.mendhak.com/run-docker-through-vpn-container/).
3. Start the VPN with: `docker-compose up -d surf`
4. Start the monitoring service with: `docker-compose up black_ring`

### Acknowledgements

This project is based on [EchterAlsFake/PHUB](https://github.com/EchterAlsFake/PHUB). Kudos to the maintainer.