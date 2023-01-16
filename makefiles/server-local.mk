### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

local: ## Install server with its dependencies
	docker-compose -f docker-compose-local.yml down && docker-compose -f docker-compose-local.yml build && docker-compose -f docker-compose-local.yml up --build traefik apiserver webserver appserver

local.force: ## Install server with its dependencies
	docker-compose -f docker-compose-local.yml down && docker-compose -f docker-compose-local.yml build --no-cache --pull && docker-compose -f docker-compose-local.yml up --build --force-recreate traefik apiserver webserver appserver

local.traefik.go: ## Open service traefik with shell sh
	docker-compose -f docker-compose-local.yml exec traefik sh

local.traefik.logs: ## Show logs from service traefik
	docker-compose -f docker-compose-local.yml logs traefik

local.apiserver.go: ## Open service apiserver with shell bash
	docker-compose -f docker-compose-local.yml exec apiserver bash

local.apiserver.logs: ## Show logs from service apiserver
	docker-compose -f docker-compose-local.yml logs apiserver

local.appserver.go: ## Open service appserver with shell bash
	docker-compose -f docker-compose-local.yml exec appserver bash

local.appserver.logs: ## Show logs from service appserver
	docker-compose -f docker-compose-local.yml logs appserver

local.server.install: ## Install server with its dependencies
	docker-compose -f docker-compose-local.yml run --rm apiserver poetry install

local.server.start: ## Start server in its docker container
	docker-compose -f docker-compose.yml up --build traefik apiserver webserver appserver

local.server.bash: ## Connect to server to lauch commands
	docker-compose -f docker-compose-local.yml exec apiserver bash

local.server.daemon: ## Start daemon server in its docker container
	docker-compose -f docker-compose-local.yml up -d apiserver

local.server.stop: ## Start server in its docker container
	docker-compose -f docker-compose-local.yml stop

local.server.logs: ## Display server logs
	tail -f server.log

local.server.upgrade: ## Upgrade pip dependencies
	docker-compose -f docker-compose-local.yml run --rm apiserver bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-local.txt --skip-virtualenv-check"

local.server.network: ## Create network netpublic
	docker network create netpublic
