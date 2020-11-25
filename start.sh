#!/bin/sh
if [ -z "$1" ]
then
      echo "\$1 is blank. Please run as like below\nsh start.sh https://google.com/"
      exit 0
fi
> .env
cat > .env <<EOF
URL=$1
EOF
a=`docker-compose up`
python parse.py -s "$a"

