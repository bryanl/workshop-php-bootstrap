#!/bin/bash
chown www-data:www-data /app -R

if [ "$ALLOW_OVERRIDE" = "**False**" ]; then
    unset ALLOW_OVERRIDE
else
    sed -i "s/AllowOverride None/AllowOverride All/g" /etc/apache2/apache2.conf
    a2enmod rewrite
fi

rm /var/www/db.ini
echo "username = ${DB_ENV_MYSQL_USER}" >> /var/www/db.ini
echo "password = ${DB_ENV_MYSQL_PASS}" >> /var/www/db.ini
echo "dbname = myapp" >> /var/www/db.ini
echo "server = ${DB_PORT_3306_TCP_ADDR}" >> /var/www/db.ini

source /etc/apache2/envvars
tail -F /var/log/apache2/* &
exec apache2 -D FOREGROUND
