codestyle:
	pycodestyle setup.py
	pycodestyle DeceptionLogicAPI/__init__.py
	pycodestyle DeceptionLogicAPI/DeceptionLogicAPI.py
	pycodestyle example.py

fix-codestyle:
	autopep8 --in-place --aggressive setup.py
	autopep8 --in-place --aggressive DeceptionLogicAPI/__init__.py
	autopep8 --in-place --aggressive DeceptionLogicAPI/DeceptionLogicAPI.py
	autopep8 --in-place --aggressive example.py

lint:
	pylint setup.py
	pylint DeceptionLogicAPI/__init__.py
	pylint DeceptionLogicAPI/DeceptionLogicAPI.py
	pylint example.py

env:
	virtualenv -p python .env

env3:
	virutalenv -p python3 .env3

wheel:
	python setup.py bdist_wheel --universal

publish:
	twine upload dist/*