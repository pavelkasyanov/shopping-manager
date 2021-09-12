create_dockers:
	-docker run --name $(PROJECT)_db -p 5432:5432 -d postgres

start_dockers: create_dockers
	docker start $(PROJECT)_db

stop_dockers:
	docker stop $(PROJECT)_db

remove_dockers: stop_dockers
	docker rm $(PROJECT)_db

create_db:
	-docker exec -i $(PROJECT)_db bash -c 'psql -h localhost -U postgres -c "CREATE DATABASE $(DB_NAME);"'

