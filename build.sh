#!/bin/bash

docker-compose build
docker tag `docker images | grep 'stevebrownlee_apihost' | awk '{ print $3 }'` stevebrownlee/api
