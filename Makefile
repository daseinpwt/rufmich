.PHONY: dist clean

dist:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/