# Install Required

#

## Windows(WAMP)

Download and Install from [HERE](https://www.apachefriends.org/download.html)

#

## Linux(LAMP)

```
sudo apt install apache2 php mariadb-server
```

```
systemctl status apache2
systemctl status mariadb.service
sudo systemctl restart apache2
sudo systemctl restart mariadb.service
```

Open With Browser: http://localhost/

```
sudo mysql_secure_installation
```

```
sud mysql -u root -p
```

```sql
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';
FLUSH PRIVILEGES;
```

```
cd /var/www/
sudo chown -R user:user html
```

```
sudo apt install phpmyadmin
```

```
cd /var/www/html
ls /usr/share/phpmyadmin
ln -s /usr/share/phpmyadmin .
sudo systemctl restart apache2
```

Open With Browser: http://localhost/phpmyadmin/

```
python -m pip install mysql-connector
```
