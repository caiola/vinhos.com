### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

dev: ## Install server with its dependencies
	docker-compose -f docker-compose-dev.yml down && docker-compose -f docker-compose-dev.yml build && docker-compose -f docker-compose-dev.yml up --build traefik apiserver webserver appserver

prod: ## Install server with its dependencies
	docker-compose -f docker-compose-prod.yml down && docker-compose -f docker-compose-prod.yml build && docker-compose -f docker-compose-prod.yml up --build traefik apiserver webserver appserver

gotraefik: ## Install server with its dependencies
	docker-compose exec traefik sh

server.install: ## Install server with its dependencies
	docker-compose run --rm apiserver poetry install

server.start: ## Start server in its docker container
	docker-compose -f docker-compose.yml up --build traefik apiserver webserver appserver

server.bash: ## Connect to server to lauch commands
	docker-compose exec apiserver bash

server.daemon: ## Start daemon server in its docker container
	docker-compose up -d apiserver

server.stop: ## Start server in its docker container
	docker-compose stop

server.logs: ## Display server logs
	tail -f server.log

server.upgrade: ## Upgrade pip dependencies
	docker-compose run --rm apiserver bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check"

server.network: ## Create network netpublic
	docker network create netpublic
