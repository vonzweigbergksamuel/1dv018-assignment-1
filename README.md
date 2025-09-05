## Requirements

- Python 3.13+

## Using uv

- Install uv: see `https://docs.astral.sh/uv/getting-started/installation/`
- Sync dependencies and create venv: `uv sync`

- `uv run main.py`

## Using pip

- Create a virtual environment
  - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
  - Windows (PowerShell): `py -m venv .venv; .venv\\Scripts\\Activate.ps1`
- Upgrade pip: `python -m pip install --upgrade pip`
- Install dependencies: `pip install matplotlib`

- `python main.py`

## Optional (dev tools)

- Lint/format: `pip install ruff`
- `ruff check`
- `ruff format`

## Notes
