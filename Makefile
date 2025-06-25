start-db:
	docker-compose up -d events_face_db

stop-db:
	docker-compose stop events_face_db

down:
	docker-compose down --volumes
