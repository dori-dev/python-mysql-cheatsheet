if you have error :)

- Windows
https://www.apachefriends.org/download.html

- Linux

sudo apt install apache2 php mariadb-server
http://localhost/
systemctl status apache2
systemctl status mariadb.service
sudo systemctl restart apache2
sudo systemctl restart mariadb.service

sudo mysql_secure_installation

sud mysql -u root -p

CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';
FLUSH PRIVILEGES;


cd /var/www/html
sudo chown -R user:user html

sudo apt install phpmyadmin

http://localhost/phpmyadmin/


cd /var/www/html
cd /usr/share/phpmyadmin
ln -s /usr/share/phpmyadmin .
http://localhost/phpmyadmin/
sudo systemctl restart apache2
http://localhost/phpmyadmin/

