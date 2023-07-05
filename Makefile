up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs app -f

restart:
	make down
	make up

rebuild:
	docker compose down -v
	docker compose up -d --build
	docker image prune -a -f