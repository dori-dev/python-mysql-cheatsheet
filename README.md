# Python MYSQL CheatSheet

Python mysql cheatsheet.

#

# Install Required

#

## Windows(WAMP)

Download and Install from [HERE](https://www.apachefriends.org/download.html)

#

## Linux(LAMP)

install packages.

```
sudo apt install apache2 php mariadb-server
```

setup packages.

```
systemctl status apache2
systemctl status mariadb.service
sudo systemctl restart apache2
sudo systemctl restart mariadb.service
```

Open With Browser: http://localhost/

setup mysql.

```
sudo mysql_secure_installation
```

use mysql.

```
sud mysql -u root -p
```

add mysql user.

```sql
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';
FLUSH PRIVILEGES;
```

change access level apache directory.

```
cd /var/www/
sudo chown -R user:user html
```

install phpmyadmin.

```
sudo apt install phpmyadmin
```

setup phpmyadmin.

```
cd /var/www/html
ls /usr/share/phpmyadmin
ln -s /usr/share/phpmyadmin .
sudo systemctl restart apache2
```

Open With Browser: http://localhost/phpmyadmin/

install mysql connector for python.

```
python -m pip install mysql-connector
```
