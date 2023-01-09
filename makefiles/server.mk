### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

dev: ## Install server with its dependencies
	docker network create netpublic &&
	docker-compose -f docker-compose-deploy.yml up --build traefik apiserver webserver app1

server.install: ## Install server with its dependencies
	docker-compose -f docker-compose-deploy.yml run --rm apiserver poetry install

server.start: ## Start server in its docker container
	docker-compose -f docker-compose-deploy.yml up traefik apiserver webserver app1

server.bash: ## Connect to server to lauch commands
	docker-compose -f docker-compose-deploy.yml exec apiserver bash

server.daemon: ## Start daemon server in its docker container
	docker-compose -f docker-compose-deploy.yml up -d apiserver

server.stop: ## Start server in its docker container
	docker-compose -f docker-compose-deploy.yml stop

server.logs: ## Display server logs
	docker-compose -f docker-compose-deploy.yml logs apiserver

server.upgrade: ## Upgrade pip dependencies
	docker-compose -f docker-compose-deploy.yml run --rm apiserver bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check"

server.network: ## Create network netpublic
	docker network create netpublic
