setup:
	pip install -r requirements.txt || true

test:
	pytest

spec-check:
	@echo "Spec check placeholder"
