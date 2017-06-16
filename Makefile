build: src/build.py src/template_mailer.jinja.py src/compose.py
	. venv/bin/activate; \
	cd src; python build.py;

test: build tests/test_mailer.py
	. venv/bin/activate; \
	py.test tests;

init:
	virtualenv venv -p python3; \
	. venv/bin/activate; \
	pip install pytest jinja2;
