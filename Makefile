build: src/build.py src/template_mailer.jinja.py
	cd src; python build.py

test: build tests/test_mailer.py
	py.test tests
