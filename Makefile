codestyle:
	pycodestyle setup.py
	pycodestyle deceptionlogic/__init__.py
	pycodestyle deceptionlogic/api/__init__.py
	pycodestyle deceptionlogic/api/client.py
	pycodestyle example.py

fix-codestyle:
	autopep8 --in-place --aggressive setup.py
	autopep8 --in-place --aggressive deceptionlogic/__init__.py
	autopep8 --in-place --aggressive deceptionlogic/api/__init__.py
	autopep8 --in-place --aggressive deceptionlogic/api/client.py
	autopep8 --in-place --aggressive example.py

lint:
	pylint setup.py
	pylint deceptionlogic/__init__.py
	pylint deceptionlogic/api/__init__.py
	pylint deceptionlogic/api/client.py
	pylint example.py

env:
	virtualenv -p python .env

env3:
	virutalenv -p python3 .env3

wheel:
	python setup.py bdist_wheel --universal

publish:
	twine upload dist/*

clean:
	find . -name "*.pyc" -type f -delete
