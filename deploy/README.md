# Deploy to Server

### Files

`apache2.conf` - apache2 config file
Put in /etc/apache2/sites-available
Symlink to sites-enabled:
ln -s /etc/apache2/sites-available/apache2.conf /etc/apache2/sites-enabled/box_packing.conf

`nginx.conf` - nginx config file
Put in /etc/nginx/sites-available
Symlink to sites-enabled:
ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/box_packing.conf















### Reference
https://www.linode.com/docs/guides/flask-and-gunicorn-on-ubuntu/