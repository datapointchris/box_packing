Link when you find out
Link:
https://askubuntu.com/questions/767504/permissions-problems-with-var-www-html-and-my-own-home-directory-for-a-website

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
sudo chown -R ubuntu:www-data /var/www
sudo find /var/www -type d -exec chmod 2750 {} \+
sudo find /var/www -type f -exec chmod 640 {} \+