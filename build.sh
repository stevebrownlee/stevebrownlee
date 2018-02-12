#!/bin/bash

docker-compose build
docker tag `docker images | grep 'apistevebrownleecom_web' | awk '{ print $3 }'` stevebrownlee/api

