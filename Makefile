PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) rotation.py --incident 59 --timeout 5 --ack 65
