#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname
import app


sys.path.insert(0, abspath(dirname(__file__)))
application = app.app


"""
建立一个软连接
ln -s /var/www/bbs/bbs.conf /etc/supervisor/conf.d/bbs.conf

# 同时删除 /etc/nginx/sites-enabled/default,否则defalault会覆盖bbs的设置
mv /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default.bak
ln -s /var/www/bbs/bbs.nginx /etc/nginx/sites-enabled/bbs



➜  ~ cat /etc/supervisor/conf.d/bbs.conf

[program:bbs]
command=/usr/local/bin/gunicorn wsgi -c gunicorn.config.py
directory=/var/www/bbs
autostart=true
autorestart=true

"""
