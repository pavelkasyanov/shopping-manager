# usr/bin/sh
docker run --name shopping_manager_postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres
