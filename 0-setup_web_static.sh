#!/usr/bin/env bash
# Setting webservers to be ready for the web_static deployment

# installing Ngnix
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
echo "Holberton School" > /var/www/html/index.nginx-debian.html
service nginx start

# creating directories if not exists
for DIRECTORIES in /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
do
	if [[ ! -d $DIRECTORIES ]]
	then
		mkdir $DIRECTORIES
	fi
done

# creating fake HTML to test Nginx config
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# creating symbolic linked to /data/web_static/releases/test/
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
chown -R ubuntu /data/
chown -R :ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
old_string="# include snippets/snakeoil.conf;"
new_string="\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "s%$old_string%$new_string%" /etc/nginx/sites-available/default
service nginx restart
