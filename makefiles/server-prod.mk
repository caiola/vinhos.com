### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

prod: ## Install server with its dependencies
	docker-compose -f docker-compose-prod.yml down && docker-compose -f docker-compose-prod.yml build && docker-compose -f docker-compose-prod.yml up --build traefik apiserver vhostwww

prod.force: ## Install server with its dependencies
	docker-compose -f docker-compose-prod.yml down && docker-compose -f docker-compose-prod.yml build --no-cache --pull && docker-compose -f docker-compose-prod.yml up -d --build --force-recreate traefik apiserver vhostwww

prod.traefik.go: ## Open service traefik with shell sh
	docker-compose -f docker-compose-prod.yml exec traefik sh

prod.traefik.logs: ## Show logs from service traefik
	docker-compose -f docker-compose-prod.yml logs traefik

local.vhostwww.start: ## Start www.domain.tld
	docker-compose -f docker-compose-prod.yml up --build vhostwww

local.vhostwww.go: ## Open service vhostwww with shell sh
	docker-compose -f docker-compose-prod.yml exec vhostwww sh

local.vhostwww.logs: ## Show logs from service vhostwww
	docker-compose -f docker-compose-prod.yml logs vhostwww

prod.apiserver.go: ## Open service apiserver with shell bash
	docker-compose -f docker-compose-prod.yml exec apiserver bash

prod.apiserver.logs: ## Show logs from service apiserver
	docker-compose -f docker-compose-prod.yml logs apiserver

prod.appserver.go: ## Open service appserver with shell bash
	docker-compose -f docker-compose-prod.yml exec appserver bash

prod.appserver.logs: ## Show logs from service appserver
	docker-compose -f docker-compose-prod.yml logs appserver

prod.server.install: ## Install server with its dependencies
	docker-compose -f docker-compose-prod.yml run --rm apiserver poetry install

prod.server.start: ## Start server in its docker container
	docker-compose -f docker-compose.yml up --build traefik apiserver webserver appserver

prod.server.bash: ## Connect to server to lauch commands
	docker-compose -f docker-compose-prod.yml exec apiserver bash

prod.server.daemon: ## Start daemon server in its docker container
	docker-compose -f docker-compose-prod.yml up -d apiserver

prod.server.stop: ## Start server in its docker container
	docker-compose -f docker-compose-prod.yml stop

prod.server.logs: ## Display server logs
	tail -f server.log

prod.server.upgrade: ## Upgrade pip dependencies
	docker-compose -f docker-compose-prod.yml run --rm apiserver bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-prod.txt --skip-virtualenv-check"

prod.server.network: ## Create network netpublic
	docker network create netpublic
