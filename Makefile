DOCKER_COMPOSE_MAIN = docker-compose.yml
DOCKER_COMPOSE_MAIN_CMD = docker compose -f $(DOCKER_COMPOSE_MAIN) 

run_app:
	$(DOCKER_COMPOSE_MAIN_CMD) up app -d --build

run_app_debug:
	$(DOCKER_COMPOSE_MAIN_CMD) up app_debug -d --build

stop_all:
	@echo "Остановка всех контейнеров..."
	@docker ps -q | xargs docker stop
