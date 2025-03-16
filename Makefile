.PHONY: run test run-prod

run:
	@flask run --debug -p 8080

run-prod:
	@flask run -p 8080

test:
	@python3 test.py