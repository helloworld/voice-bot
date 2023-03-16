black:
	black --fast . 

ruff:
	ruff --fix .

check_ruff:
	ruff .

fix_all:
	make black
	make ruff

install_dev_python_modules_verbose:
	python scripts/install_dev_python_modules.py

dev_install: install_dev_python_modules_verbose 

