#!/bin/sh

echo "mkdir /var/cache/etcd2prop; chmod 777 /var/cache/etcd2prop" > /tmp/postinstall.sh
fpm -s dir -t rpm \
    -n etcd2prop -v 0.1 --iteration=0 \
    --rpm-user=root --description="Copy etcd store to java properties file" \
    --after-install=/tmp/postinstall.sh ../etcd2prop.py=/usr/bin/etcd2prop
