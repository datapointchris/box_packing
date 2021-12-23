# Deploy to Server

### Files

`apache2.conf` - apache2 config file
Put in /etc/apache2/sites-available
Symlink to sites-enabled:
ln -s /etc/apache2/sites-available/apache2.conf /etc/apache2/sites-enabled/box_packing.conf

`nginx.conf` - nginx config file
Put in /etc/nginx/sites-available
Symlink to sites-enabled:
ln -s /etc/nginx/sites-available/box_packing /etc/nginx/sites-enabled/box_packing


`supervisor.conf` - supervisor config file
Put in /etc/supervisor/conf.d/

Create log directories as specified in `supervisor.conf`

sudo mkdir /var/log/box_packing
sudo touch /var/log/box_packing/out.log
sudo touch /var/log/box_packing/err.log


# Apache Permissions

## Allow Apache access to the folders and the files
sudo chgrp -R www-data /var/www
sudo find /var/www -type d -exec chmod g+rx {} +
sudo find /var/www -type f -exec chmod g+r {} +

## Give web server write permissions to the folder and db file
sudo chmod g+w /var/www/box_packing/box_packing
sudo chmod g+w /var/www/box_packing/box_packing/moving.db

## Give owner read/write privileges to the folders and files
sudo chown -R $USER /var/www
sudo find /var/www -type d -exec chmod u+rwx {} +
sudo find /var/www -type f -exec chmod u+rw {} +

## Make sure every new file after is created with www-data as the access user
sudo find /var/www -type d -exec chmod g+s {} +


## SHORTCUT for the first 8 commands
sudo chown -R $USER:www-data /var/www
sudo find /var/www -type d -exec chmod 2750 {} \+
sudo find /var/www -type f -exec chmod 640 {} \+


# Reference
https://www.linode.com/docs/guides/flask-and-gunicorn-on-ubuntu/

https://dlukes.github.io/flask-wsgi-url-prefix.html#mwe

