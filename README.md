docker run --name mynews-docker -e POSTGRES_PASSWORD=secret -p 5432:5432 -d postgres

docker exec -it mynews-docker bash

psql -h localhost -U postgres

CREATE DATABASE mynews;
CREATE USER mynewsuser WITH PASSWORD 'secret';
ALTER ROLE mynewsuser SET client_encoding TO 'utf8';
ALTER ROLE mynewsuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE mynewsuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mynews TO mynewsuser;
\q
