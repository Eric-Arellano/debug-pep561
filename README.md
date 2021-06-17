# Debug PEP 561

To use:

1. Install Poetry, e.g. `pipx install poetry`.
2. `cd poetry_runner`
3. Update `pyproject.toml` to point to the wheel you want to test. If you changed it, do `poetry lock` then `poetry install`.
4. `poetry run mypy app.py --cache-dir=/dev/null

