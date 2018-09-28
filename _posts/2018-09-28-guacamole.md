---
title:  "Guacamole"
tags:
  - guacamole
  - tutorial
---

```shell
mkdir sql-scripts
cd sql-scripts
docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --postgres > initdb.sql
wget user.sql
cd ..
```

```shell
nano Dockerfile
```
```shell
FROM postgres
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/
```

```shell
docker build -t some-postgres .
docker run -d --name some-postgres \
 -e POSTGRES_USER=guacamole \
 -e POSTGRES_PASSWORD=guacamole \
 some-postgres
```

```shell
docker exec -it some-postgres bash
psql -U guacamole -c "select * from guacamole_user;"
```

```shell
docker run --name some-guacd -d guacamole/guacd

docker run --name some-guacamole    \
    --link some-guacd:guacd         \
    --link some-postgres:postgres   \
    -e POSTGRES_DATABASE=guacamole    \
    -e POSTGRES_USER=guacamole    \
    -e POSTGRES_PASSWORD=guacamole \
    -d -p 8080:8080 guacamole/guacamole

docker logs some-guacamole
```

http://localhost:8080/guacamole
user: guacadmin
password: guacadmin
