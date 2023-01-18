# /data/

is a volume folder shared with containers

# /data/traefik/acme.json

The SSL certificates are going to be stored in a json file inside the letsencrypt directory. For Let's Encrypt to work we are going to create the file, fill it with an empty json object and set the needed permissions.

```
# sudo mkdir -p /opt/docker/vinhos.com/conf/traefik/traefikdynamic

# fill the file with an empty json object
echo "{}" > /opt/docker/vinhos.com/data/letsencrypt/acme.json

# Set the permissions
sudo chmod 0600 /opt/docker/vinhos.com/data/letsencrypt/acme.json

sudo mkdir -p /opt/docker/traefik/logs
sudo touch /opt/docker/traefik/logs/traefik.log
```


