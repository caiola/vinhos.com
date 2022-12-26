### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

dev: ## Install server with its dependencies
	docker-compose up --build apiserver nginx

server.install: ## Install server with its dependencies
	docker-compose run --rm apiserver pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location

server.start: ## Start server in its docker container
	docker-compose up apiserver

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
