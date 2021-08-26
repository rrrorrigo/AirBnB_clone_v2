#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt install -y nginx
sudo mkdir data && cd data
sudo mkdir web_static && cd web_static
sudo mkdir releases shared && cd releases
sudo mkdir test && cd test
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > index.html
cd /data/web_static
sudo mkdir current
sudo ln -sf current /data/web_static/releases/test/
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo sed -i "$ d" /etc/nginx/sites-available/default
sudo echo "location /hbnb_static {
alias /data/web_static/current/;
error_page  404  /404.html;
try_files $uri $uri/ =404;
}
}
" >> /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
