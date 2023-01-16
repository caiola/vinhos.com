### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

dev: ## Install server with its dependencies
	docker-compose -f docker-compose-dev.yml down && docker-compose -f docker-compose-dev.yml build && docker-compose -f docker-compose-dev.yml up --build traefik apiserver appserver

dev.force: ## Install server with its dependencies
	docker-compose -f docker-compose-dev.yml down && docker-compose -f docker-compose-dev.yml build --no-cache --pull && docker-compose -f docker-compose-dev.yml up --build --force-recreate traefik apiserver appserver

dev.traefik.go: ## Open service traefik with shell sh
	docker-compose -f docker-compose-dev.yml exec traefik sh

dev.traefik.logs: ## Show logs from service traefik
	docker-compose -f docker-compose-dev.yml logs traefik

dev.apiserver.go: ## Open service apiserver with shell bash
	docker-compose -f docker-compose-dev.yml exec apiserver bash

dev.apiserver.logs: ## Show logs from service apiserver
	docker-compose -f docker-compose-dev.yml logs apiserver

dev.appserver.go: ## Open service appserver with shell bash
	docker-compose -f docker-compose-dev.yml exec appserver bash

dev.appserver.logs: ## Show logs from service appserver
	docker-compose -f docker-compose-dev.yml logs appserver

dev.server.install: ## Install server with its dependencies
	docker-compose -f docker-compose-dev.yml run --rm apiserver poetry install

dev.server.start: ## Start server in its docker container
	docker-compose -f docker-compose.yml up --build traefik apiserver webserver appserver

dev.server.bash: ## Connect to server to lauch commands
	docker-compose -f docker-compose-dev.yml exec apiserver bash

dev.server.daemon: ## Start daemon server in its docker container
	docker-compose -f docker-compose-dev.yml up -d apiserver

dev.server.stop: ## Start server in its docker container
	docker-compose -f docker-compose-dev.yml stop

dev.server.logs: ## Display server logs
	tail -f server.log

dev.server.upgrade: ## Upgrade pip dependencies
	docker-compose -f docker-compose-dev.yml run --rm apiserver bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check"

dev.server.network: ## Create network netpublic
	docker network create netpublic
