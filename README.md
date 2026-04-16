# PyApiSample - Automated Test Framework

This repository houses a modular API testing framework built with Python. It is designed around the `pytest` runner and utilizes `httpx` for synchronous HTTP communications. Dependency resolution and toolchain management are handled by the `uv` package manager, ensuring extremely fast environment isolation and execution.

## Architectural Overview

The test suite incorporates industry-standard conventions:
- **Core Abstraction Layer (`core/`)**: Standardizes API interactions by wrapping endpoint calls and environment configurations.
- **Fixture Provisioning (`tests/conftest.py`)**: Centralizes the `pytest` session state and data creation hooks (e.g., dynamically provisioning temporary resources for testing schemas).
- **Arrange-Act-Assert Syntax (`tests/`)**: Test modules strictly enforce the AAA logical methodology to maintain robust readability over testing suites.
- **Environment Targeting (`.env`)**: Integrates flexible environment boundaries managed by `python-dotenv`.
- **Linting Rigor**: Utilizes `ruff` to firmly enforce type checking (`typing`) alongside code quality and PEP 8 guidelines.

## Prerequisites

To execute this testing framework locally, ensure you have the following installed:
- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (Astral's high-performance Python package manager).

## Getting Started

### 1. Clone the Repository
Clone the framework to your preferred local directory:
```bash
git clone https://github.com/chinmaymudholkar/PyApiSample.git
cd PyApiSample
```

### 2. Environment Configuration
The framework reads the base URL from the `.env` file.  While this file is generally not added to the git repo, I've added it here to ensure
an `.env` file exists at the root of the project with the requisite base properties for demo purposes.
```env
BASE_URL=https://jsonplaceholder.typicode.com
```

### 3. Installation
`uv` is used to manage all project dependencies.  It also manages all virtual environments automatically based on the
mappings defined in `pyproject.toml`.
```bash
uv sync
```
*(Note: If you run individual `uv run` commands directly, `uv` will implicitly parse and map missing dependencies without needing an explicit sync command).*

## Test Execution

### Running Tests
To trigger the automated testing suite and evaluate all defined assertions:
```bash
uv run pytest
```

### Validation and Linting
We use ruff to evaluate code compliance against standard security protocols, typing syntax, and implicit structure conventions.  To lint your changes:
```bash
uv run ruff check
```
To format your code:
```bash
uv run ruff format
```
To process auto-formattable linting exceptions:
```bash
uv run ruff check --fix
```

### Coming soon...
- Reporting using Allure reports
- Execution using GitHub Actions
