codestyle:
	pycodestyle setup.py
	pycodestyle deceptionlogic/__init__.py
	pycodestyle deceptionlogic/api/__init__.py
	pycodestyle deceptionlogic/api/client.py
	pycodestyle deceptionlogic/aws/__init__.py
	pycodestyle deceptionlogic/aws/ec2.py
	pycodestyle deceptionlogic/bin/deception
	pycodestyle example.py

fix-codestyle:
	autopep8 --in-place --aggressive setup.py
	autopep8 --in-place --aggressive deceptionlogic/__init__.py
	autopep8 --in-place --aggressive deceptionlogic/api/__init__.py
	autopep8 --in-place --aggressive deceptionlogic/api/client.py
	autopep8 --in-place --aggressive deceptionlogic/aws/__init__.py
	autopep8 --in-place --aggressive deceptionlogic/aws/ec2.py
	autopep8 --in-place --aggressive deceptionlogic/bin/deception
	autopep8 --in-place --aggressive example.py

lint:
	pylint setup.py
	pylint deceptionlogic/__init__.py
	pylint deceptionlogic/api/__init__.py
	pylint deceptionlogic/api/client.py
	pylint deceptionlogic/aws/__init__.py
	pylint deceptionlogic/aws/ec2.py
	pylint deceptionlogic/bin/deception
	pylint --disable=W example.py

install:
	pip install --upgrade -r requirements.txt

env:
	virtualenv -p python .env
	.env/bin/pip install --upgrade -r requirements.txt

env3:
	python3 -m venv .env3
	.env3/bin/pip install --upgrade pip
	.env3/bin/pip install --upgrade -r requirements.txt

wheel:
	-rm dist/*
	python setup.py bdist_wheel --universal

publish:
	twine upload --skip-existing dist/*

local-install:
	pip uninstall -y deceptionlogic
	pip install dist/*

clean:
	find . -name "*.pyc" -type f -delete
	rm -rf dist
