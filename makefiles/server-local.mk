### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

local: ## Install server with its dependencies
	docker-compose -f docker-compose-local.yml down && docker-compose -f docker-compose-local.yml build && docker-compose -f docker-compose-local.yml up --build traefik apiserver appserver

force: ## Install server with its dependencies
	docker-compose -f docker-compose-local.yml down && docker-compose -f docker-compose-local.yml build --no-cache --pull && docker-compose -f docker-compose-local.yml up --build --force-recreate traefik apiserver appserver

traefik.go: ## Open service traefik with shell sh
	docker-compose -f docker-compose-local.yml exec traefik sh

traefik.logs: ## Show logs from service traefik
	docker-compose -f docker-compose-local.yml logs traefik

apiserver.go: ## Open service apiserver with shell bash
	docker-compose -f docker-compose-local.yml exec apiserver bash

apiserver.logs: ## Show logs from service apiserver
	docker-compose -f docker-compose-local.yml logs apiserver

appserver.go: ## Open service appserver with shell bash
	docker-compose -f docker-compose-local.yml exec appserver bash

appserver.logs: ## Show logs from service appserver
	docker-compose -f docker-compose-local.yml logs appserver

localserver.install: ## Install server with its dependencies
	docker-compose -f docker-compose-local.yml run --rm apiserver poetry install

localserver.start: ## Start server in its docker container
	docker-compose -f docker-compose.yml up --build traefik apiserver webserver appserver

localserver.bash: ## Connect to server to lauch commands
	docker-compose -f docker-compose-local.yml exec apiserver bash

localserver.daemon: ## Start daemon server in its docker container
	docker-compose -f docker-compose-local.yml up -d apiserver

localserver.stop: ## Start server in its docker container
	docker-compose -f docker-compose-local.yml stop

localserver.logs: ## Display server logs
	tail -f server.log

localserver.upgrade: ## Upgrade pip dependencies
	docker-compose -f docker-compose-local.yml run --rm apiserver bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-local.txt --skip-virtualenv-check"

localserver.network: ## Create network netpublic
	docker network create netpublic
