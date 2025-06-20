
run:
	docker compose up

delete:
	docker compose down --remove-orphans

migrate:
	docker compose run web uv run python manage.py migrate

migrations:
	docker compose run web uv run python manage.py makemigrations

shell:
	docker compose run web uv run python manage.py shell

test:
	docker compose run web uv run python manage.py test