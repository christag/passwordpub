#!/bin/bash
apt-get update && apt-get upgrade -y
apt-get install certbot nginx -y

service nginx start

mkdir /var/www/passwordpub.com

cat << EOF > /etc/nginx/sites-available/default
server {
    listen 80;
    server_name passwordpub.com;
	index index.html index.php;
    root /var/www/passwordpub.com;
    location ~ /.well-known {
		allow all;
	}
}
EOF

serice nginx restart

certbot certonly --webroot --email chris.tagliaferro@gmail.com -w /var/www/passwordpub.com -d passwordpub.com --agree-tos --no-eff-email --dry-run

/bin/bash