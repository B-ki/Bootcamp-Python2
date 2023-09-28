ENV_FILE = .ENV_FILE
DOCKER = DOCKER
COMPOSE = $(DOCKER) compose --env-file $(ENV_FILE)

all: build up

build:
	curl -LO https://cdn.intra.42.fr/document/document/17536/subject.zip
	unzip subject.zip
	rm subject.zip
	sudo mv subject/ data/
	rm -rf subject
	docker compose build

up:
	docker compose up -d

clean:
	docker container rm -f postgres

fclean: clean
	sudo rm -rf ./data
	mkdir ./data

re: fclean all

.PHONY: re up build clean fclean
