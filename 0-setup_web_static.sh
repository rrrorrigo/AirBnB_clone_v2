#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt install -y nginx
mkdir data && cd data
mkdir web_static && cd web_static
mkdir releases shared && cd releases
mkdir test && cd test
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > index.html
cd /data/web_static
mkdir current
ln -sf current /data/web_static/releases/test/
chown -R ubuntu /data/
chgrp -R ubuntu /data/
sed -i "$ d" /etc/nginx/sites-available/default
echo "location /hbnb_static {
alias /data/web_static/current/;
error_page  404  /404.html;
try_files $uri $uri/ =404;
}
}
" >> /etc/nginx/sites-available/default
service nginx restart
exit 0
