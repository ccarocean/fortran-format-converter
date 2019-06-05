.PHONY: all init check test coverage html pdf clean clean-all apidoc

module=fortran_format_converter

all:
	@echo 'init             install development requirements'
	@echo 'todo             list TODO statements (requires grep)'
	@echo 'check            run static code checkers'
	@echo 'test             run unit tests'
	@echo 'coverage         generate HTML coverage report'
	@echo 'html             build HTML documentation'
	@echo 'pdf              build PDF documentation (requires LaTeX)'
	@echo 'package          build source and binary packages'
	@echo 'clean            cleanup source tree'
	@echo 'clean-all        also removes tox and eggs'


init:
	@pip install -q -r dev-requirements.txt

todo:
	@grep -roIn --color 'TODO:.*' $(module) tests docs

test: check
	@python -m pytest -v --cov=$(module) --cov-branch

coverage: check
	@python -m pytest -v --cov=$(module) --cov-branch \
		--cov-report html

check:
	@mypy $(module)
	# @mypy --config-file tests/mypy.ini tests
	@flake8 $(module) # tests
	@python -m pylint $(module)
	@python -m pycodestyle $(module) # tests
	@python -m pydocstyle $(module)

apidoc: export SPHINX_APIDOC_OPTIONS=members,no-undoc-members,show-inheritance,private-members,special-members
apidoc:
	@sphinx-apidoc -o docs/api -e $(module)
	@rm docs/api/modules.rst

html: apidoc
	@$(MAKE) -C docs html

pdf: apidoc
	@$(MAKE) -C docs latexpdf

package: test
	@python setup.py sdist
	@python setup.py bdist_wheel
	@twine check dist/*

clean:
	@rm -f docs/api/*.rst
	@rm -f dataclass_builder/*.pyc
	@rm -f tests/*.pyc
	@rm -rf tests/.pytest_cache
	@rm -f tests/.coverage
	@rm -f .coverage
	@rm -rf htmlcov
	@rm -rf __pycache__ dataclass_builder/__pycache__ tests/__pycache__
	@rm -rf *.egg-info
	@rm -rf dist
	@rm -rf build

clean-all: clean
	@rm -rf .tox
	@rm -rf .eggs
	@$(MAKE) -C docs clean
