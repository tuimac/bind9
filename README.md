# Bind9 on docker

This docker image is installed bind9. If you bind the port 53 of the container from this image to the host server port 53, you make the server DNS server.
Now this is just beta now.

## How to use
### Prerequisite
Disable local DNS. Because this container use as a external DNS server so it use port 53 tcp and udp.
If your host OS is ubuntu, following line can disable local DNS.(If your ubuntu version deal with
Systemd)

```
# systemctl stop systemd-resolved
```

### Deployment
You can deploy bind9 container like this,
```
docker run -itd --name bind9 -v $(pwd)/tuimac.private:/etc/bind/named/tuimac.private -p 53:53/tcp -p 53:53/udp --network="bridge" tuimac/bind9
```

## Authors

* **Kento Kashiwagi** - [tuimac](https://github.com/tuimac)

If you have some opinion and find bugs, please post [here](https://github.com/tuimac/openvpn/issues).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Plan

- Renew A record dynamically by EC2 tag.
