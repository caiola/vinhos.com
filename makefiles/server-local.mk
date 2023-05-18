### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

local: ## Install server with its dependencies
	docker-compose -f docker-compose-local.yml down && docker-compose -f docker-compose-local.yml build && docker-compose -f docker-compose-local.yml up --build apiserver vhostwww vhostapp traefik db

local.force: ## Install server with its dependencies
	docker-compose -f docker-compose-local.yml down && docker-compose -f docker-compose-local.yml build --no-cache --pull && docker-compose -f docker-compose-local.yml up --build --force-recreate apiserver vhostwww vhostapp traefik db

local.traefik.go: ## Open service traefik with shell sh
	docker-compose -f docker-compose-local.yml exec traefik sh

local.traefik.logs: ## Show logs from service traefik
	docker-compose -f docker-compose-local.yml logs traefik

local.db.start: ## Start service db
	docker-compose -f docker-compose-local.yml up --build db

local.db.go: ## Open service db with shell sh
	docker-compose -f docker-compose-local.yml exec db sh

local.db.logs: ## Show logs from service db
	docker-compose -f docker-compose-local.yml logs db

local.vhostwww.start: ## Start www.domain.tld
	docker-compose -f docker-compose-local.yml up --build vhostwww

local.vhostwww.go: ## Open service vhostwww with shell sh
	docker-compose -f docker-compose-local.yml exec vhostwww sh

local.vhostwww.logs: ## Show logs from service vhostwww
	docker-compose -f docker-compose-local.yml logs vhostwww

local.vhostapp.start: ## Start app.domain.tld
	docker-compose -f docker-compose-local.yml up --build vhostapp

local.vhostapp.go: ## Open service vhostapp with shell sh
	docker-compose -f docker-compose-local.yml exec vhostapp sh

local.vhostapp.logs: ## Show logs from service vhostapp
	docker-compose -f docker-compose-local.yml logs vhostapp

local.apiserver.go: ## Open service apiserver with shell bash
	docker-compose -f docker-compose-local.yml exec apiserver sh

local.apiserver.routes: ## Open service apiserver and run command to show routes
	docker-compose -f docker-compose-local.yml exec apiserver flask routes

local.apiserver.migrations: ## Run migrations
	docker-compose -f docker-compose-local.yml exec apiserver flask db upgrade

local.apiserver.migrations.upgrade: ## Upgrade migrations
	docker-compose -f docker-compose-local.yml exec apiserver sh -c "cd /app/ && flask db upgrade"

local.apiserver.run: ## Open service apiserver with shell bash
	docker-compose -f docker-compose-local.yml build && docker-compose -f docker-compose-local.yml up --build apiserver

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
