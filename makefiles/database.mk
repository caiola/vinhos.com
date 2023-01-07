### DATABASE
# ¯¯¯¯¯¯¯¯


database.connect: ## Connect to database
	docker-compose -f docker-compse.deploy.yml exec db psql -Upostgres

database.migrate: ## Create alembic migration file
	docker-compose -f docker-compse.deploy.yml run --rm apiserver python manage.py db migrate

database.upgrade: ## Upgrade to latest migration
	docker-compose -f docker-compse.deploy.yml run --rm apiserver python manage.py db upgrade

database.downgrade: ## Downgrade latest migration
	docker-compose -f docker-compse.deploy.yml run --rm apiserver python manage.py db downgrade
