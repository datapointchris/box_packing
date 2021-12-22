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


`gunicorn.conf` - gunicorn config file



`supervisor.conf` - supervisor config file
Put in /etc/supervisor/conf.d/

Create log directories as specified in `supervisor.conf`

sudo mkdir /var/log/box_packing
sudo touch /var/log/box_packing/out.log
sudo touch /var/log/box_packing/err.log











### Reference
https://www.linode.com/docs/guides/flask-and-gunicorn-on-ubuntu/