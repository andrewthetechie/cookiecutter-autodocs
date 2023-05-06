.DEFAULT_GOAL := help build

# This help function will automatically generate help/usage text for any make target that is commented with "##".
# Targets with a singe "#" description do not show up in the help text
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'

build-gha: ## build a docker image for use with gha locally
	docker build -t cookiecutter-autodocs-gha -f Docker/GHA-Dockerfile .

build-pc: ## build a docker image for use with pre-commit locally
	docker build -t cookiecutter-autodocs-pc -f Docker/PC-Dockerfile .
