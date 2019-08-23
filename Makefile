
#install_venv:
#  virtualenv .venv -p /usr/local/bin/python3.7
#install:
##	( \
###	source $(BIN)activate; \
#	pip install -r requirements.txt; \
#	)

run:
	python src/main.py

#venv: source .venv/bin/activate

#clean:
#	rm -rf .venv
# 	find -iname "*.pyc" -delete
