### FORK FROM [LINUXSERVER](https://github.com/linuxserver/docker-transmission)


## Usage

Here are some example snippets to help you get started creating a container.

### docker-compose (recommended, [click here for more info](https://docs.linuxserver.io/general/docker-compose))

```yaml
---
version: "2.1"
services:
  transmission:
    image: kissyouhunter/transmission:latest
    container_name: transmission
    environment:
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - USER=username #optional
      - PASS=password #optional
    volumes:
      - /path/to/data:/config
      - /path/to/downloads:/downloads
      - /path/to/watch/folder:/watch
    ports:
      - 9091:9091
      - 51413:51413
      - 51413:51413/udp
    restart: unless-stopped
```

### docker cli ([click here for more info](https://docs.docker.com/engine/reference/commandline/cli/))

```bash
docker run -d \
  --name=transmission \
  -e PUID=0 \
  -e PGID=0 \
  -e TZ=Asia/Shanghai \
  -e USER=username `#optional` \
  -e PASS=password `#optional` \
  -p 9091:9091 \
  -p 51413:51413 \
  -p 51413:51413/udp \
  -v /path/to/data:/config \
  -v /path/to/downloads:/downloads \
  -v /path/to/watch/folder:/watch \
  --restart unless-stopped \
  kissyouhunter/transmission:latest
```

## Parameters

Container images are configured using parameters passed at runtime (such as those above). These parameters are separated by a colon and indicate `<external>:<internal>` respectively. For example, `-p 8080:80` would expose port `80` from inside the container to be accessible from the host's IP on port `8080` outside the container.

| Parameter | Function |
| :----: | --- |
| `-p 9091` | WebUI |
| `-p 51413` | Torrent Port TCP |
| `-p 51413/udp` | Torrent Port UDP |
| `-e PUID=1000` | for UserID - see below for explanation |
| `-e PGID=1000` | for GroupID - see below for explanation |
| `-e TZ=Europe/London` | Specify a timezone to use EG Europe/London. |
| `-e TRANSMISSION_WEB_HOME=/combustion-release/` | Specify an alternative UI options are [`/combustion-release/`](https://github.com/Secretmapper/combustion), [`/transmission-web-control/`](https://github.com/ronggang/transmission-web-control), [`/kettu/`](https://github.com/endor/kettu), [`/flood-for-transmission/`](https://github.com/johman10/flood-for-transmission), and [`/transmissionic/`](https://github.com/6c65726f79/Transmissionic). |
| `-e USER=username` | Specify an optional username for the interface |
| `-e PASS=password` | Specify an optional password for the interface |
| `-e WHITELIST=iplist` | Specify an optional list of comma separated ip whitelist. Fills rpc-whitelist setting. |
| `-e PEERPORT=peerport` | Specify an optional port for torrent TCP/UDP connections. Fills peer-port setting. |
| `-e HOST_WHITELIST=dnsname list` | Specify an optional list of comma separated dns name whitelist. Fills rpc-host-whitelist setting. |
| `-v /config` | Where transmission should store config files and logs. |
| `-v /downloads` | Local path for downloads. |
| `-v /watch` | Watch folder for torrent files. |
