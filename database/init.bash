#!/bin/bash

postgres -D /var/lib/postgresql/data \
       	--logging_collector=on \
       	--log_destination="stderr,csvlog" \
	--log_directory="/var/log/postgresql/" \
	--log_filename="postgresql-%Y-%m-%d.log" \
	--log_min_messages=warning &

sleep 5

psql -U postgres -c "CREATE DATABASE ${POSTGRES_DB};"
psql -U postgres -c "CREATE ROLE administrator WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD '${POSTGRES_PASSWORD}';"

wait %1
