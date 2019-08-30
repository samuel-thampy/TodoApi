
#install_venv:
#  virtualenv .venv -p /usr/local/bin/python3.7
#install:
##	( \
###	source $(BIN)activate; \
#	pip install -r requirements.txt; \
#	)

run:
	python src/main.py

create_image:
	docker build -t todo_api .

run_image:
	docker run -p 5000:5000 todo_api

coverage_test:
	python -m pytest --cov-report term --cov-report html:coverage --cov-config setup.cfg --cov=src/ test/

lint_test:
	python -m flake8 ./src ./test
    
#venv: source .venv/bin/activate

#clean:
#	rm -rf .venv
# 	find -iname "*.pyc" -delete
