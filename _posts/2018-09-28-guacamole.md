---
title:  "Guacamole"
tags:
  - guacamole
  - tutorial
---
{% include toc %}
# Postgres

## Dockerfile

```shell
mkdir sql-scripts
docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --postgres > sql-scripts/initdb.sql
```
```shell
cat <<EOF >sql-scripts/user.sql
-- Create user "myuser" with password "password"
INSERT INTO guacamole_user (username, password_hash, password_salt, password_date)
VALUES ('myuser',
    decode('5522f219fda1924b4f6d3212d1ae66d468580c5535449437d9e80eefaa883a01', 'hex'),  -- 'password'
    decode('b3fa7bbc39903666a190e63c092a90729d1cc94355625e91c63bb738f0454387', 'hex'),
    CURRENT_TIMESTAMP);


-- Grant this user create connections permission
INSERT INTO guacamole_system_permission
SELECT user_id, permission::guacamole_system_permission_type
FROM (
    VALUES
        ('myuser', 'CREATE_CONNECTION')
) permissions (username, permission)
JOIN guacamole_user ON permissions.username = guacamole_user.username;

-- Grant this user permission to read/update self
INSERT INTO guacamole_user_permission
SELECT guacamole_user.user_id, affected.user_id, permission::guacamole_object_permission_type
FROM (
    VALUES
        ('myuser', 'myuser', 'READ'),
        ('myuser', 'myuser', 'UPDATE')
) permissions (username, affected_username, permission)
JOIN guacamole_user          ON permissions.username = guacamole_user.username
JOIN guacamole_user affected ON permissions.affected_username = affected.username;
EOF
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

Check if the db was created:
```shell
docker exec -it some-postgres bash
psql -U guacamole -c "select * from guacamole_user;"
```

Run
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


## Docker-compose
```shell
git clone git@github.com:siddou/guacamole-postgres.git
cd guacamole-postgres
docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --postgres > sql-scripts/initdb.sql
docker volume create --name=postgres_database
docker-compose up -d
```

# MySQL

## Docker-compose
```shell
git clone git@github.com:siddou/guacamole-mysql.git
cd guacamole-mysql
docker run --rm guacamole/guacamole /opt/guacamole/bin/initdb.sh --mysql > sql-scripts/initdb.sql
mv .env.example .env
docker-compose up -d
```

{% include disqus.html %}