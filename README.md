# sebco-labs-testing

Mutation testing PoC for Python focused on **quality signal over quantity**.

This repository explores how mutation testing can strengthen automated test suites by revealing assertions that look correct on the surface but still allow incorrect logic to survive.

---

## Why this project exists

Traditional test metrics such as line coverage can be misleading.
A test can execute code and still fail to validate the behavior that actually matters.

This PoC uses `mutmut` together with `pytest` to answer a stronger question:

> **If the production logic changes in small but dangerous ways, do the tests really catch it?**

That is the value of mutation testing.

Instead of measuring only execution, this repo measures how well the test suite detects broken logic.

---

## What is being tested

The current PoC is centered on monthly report period generation for a user account.

The core logic lives under `lib_core/time_utils/` and covers:

- **`get_periods.py`** — builds the list of monthly periods from an account creation date
- **`date_utils.py`** — generates UTC timestamps in ISO 8601 format
- **`schedule_time.py`** — additional scheduling utilities

The main business rule validates the expected monthly periods returned from an account creation date, including date-based behavior such as:

- when the current day is **5 or later**, the latest valid period corresponds to the **previous month**
- when the current day is **before the 5th**, the latest valid period corresponds to **two months back**
- the API-style response returns **up to 12 periods**

---

## Why mutation testing matters here

This repo is intentionally small so the learning signal is easy to understand.

A normal test suite may say:

- response shape is valid
- values look correct
- ordering is correct
- boundary conditions are covered

But mutation testing goes one step further and asks:

- what happens if a comparison operator changes?
- what happens if a boundary rule shifts by one condition?
- what happens if a month calculation is subtly altered?

If those mutations survive, the suite is still missing important protection.

That makes mutation testing especially useful for:

- contract validation
- date logic
- billing and reporting periods
- boundary-driven business rules
- CI feedback quality

---

## Tech stack

| Tool | Purpose |
|---|---|
| Python | Runtime |
| `pytest` | Test runner |
| `mutmut` | Mutation testing engine |
| `pytest-html` | HTML test reports |
| `python-dateutil` | Relative date arithmetic |
| GitHub Actions | CI pipeline |
| Semantic Release | Automated versioning |

---

## Repository structure

```text
.
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       ├── pipeline.yml
│       ├── pr-governance.yml
│       └── release.yml
├── doc/
│   ├── 0. Repository Secret and SSH KEY.md
│   ├── 1. Main setup.md
│   ├── 2. Configurar-git-bash-vscode.md
│   ├── 3. Github_Action.md
│   └── 4. SetupArtifactHTMLReport.md
├── lib_core/
│   ├── labs/
│   │   └── my_code.py
│   └── time_utils/
│       ├── date_utils.py
│       ├── get_periods.py
│       └── schedule_time.py
├── tests/
│   ├── conftest.py
│   └── labs/
│       └── test_extract_period.py
├── pyproject.toml
├── pytest.ini
├── requirements.txt
├── setup.py
└── README.md
```

---

## Current test scope

The test suite lives in `tests/labs/test_extract_period.py` and is marked with `@pytest.mark.mutmut`.

### Response-oriented validation

- validates the returned `accountCreatedDate`
- validates the generated `periodList`
- validates returned length depending on account age
- validates descending order and expected title, month, and year values

### Functional rules

- includes previous month when the current day is `>= 5`
- skips previous month when the current day is `< 5`
- prevents current month from appearing when it should not
- enforces the expected month, title, and year for the first returned item

---

## Mutation scope

Mutation testing is configured in `pyproject.toml` to target only the business logic:

```toml
[tool.mutmut]
paths_to_mutate = ["lib_core/time_utils"]
tests_dir = ["tests"]
runner = "python -m pytest -m mutmut -q"
do_not_mutate = ["__init__.py"]
```

This keeps the mutation analysis focused on the time and period calculation logic rather than the whole repository.

---

## How to run locally

### 1. Create and activate a virtual environment

**macOS / Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the tests

```bash
pytest -m mutmut
```

### 4. Run mutation testing

```bash
mutmut run
```

### 5. Inspect results

```bash
mutmut results
mutmut show
```

To inspect a specific surviving mutant:

```bash
mutmut show <mutant_id>
```

---

## How to interpret the results

### Killed mutant

A mutation was introduced and the tests failed as expected.

This is the goal. It means the suite is protecting the intended behavior.

### Survived mutant

A mutation changed the logic, but the tests still passed.

This is the main learning signal. It usually means one of these is true:

- the assertion is too weak
- the wrong thing is being asserted
- a boundary case is missing
- the test executes the code but does not verify the business meaning

### Suspicious, timeout, or unsupported cases

These should be reviewed separately depending on the mutation and runtime context.

---

## CI integration

The repository includes three GitHub Actions workflows.

### `pipeline.yml`

- runs the `pytest` regression suite
- publishes HTML test results as artifacts
- runs mutation testing
- extracts surviving mutant IDs
- generates per-mutant details and diffs
- calculates mutation score
- posts a mutation summary comment on pull requests

### `pr-governance.yml`

- enforces PR naming and branching conventions

### `release.yml`

- triggers semantic versioning via `semantic-release` on merge to `main`

---

## Mutation artifacts generated in CI

The pipeline produces the following files as downloadable artifacts:

| File | Content |
|---|---|
| `mutmut-run.txt` | Full mutation run output |
| `mutmut-results.txt` | Summary of killed and survived mutations |
| `mutmut-show.txt` | All mutant details |
| `mutmut-diffs.txt` | Code diffs per mutant |
| `surviving-mutants.txt` | IDs of surviving mutants |
| `mutation-score.txt` | Final mutation score |

These artifacts make it easier to inspect what survived, understand how the mutation changed the code, and use mutation evidence in pull request reviews.

---

## Example learning outcomes from this PoC

This project is useful for identifying situations like:

- a date rule is exercised but not truly verified
- a report boundary is asserted indirectly instead of explicitly
- a list length is validated, but the content semantics are still weak
- month, title, and year combinations pass even though one business condition changed

That is exactly the kind of gap mutation testing is meant to expose.

---

## Roadmap

- expand mutation scenarios across additional business rules
- harden assertions around edge dates and ordering behavior
- compare mutation score trends over time
- reuse this pattern in broader CI governance flows
- enrich PR feedback using mutation evidence as a first-class signal

---

## Who this is for

This repository is useful for people interested in:

- QA Engineering and SDET practices
- backend automation
- CI quality signals
- mutation testing with Python
- contract and business-rule validation

---

## Author

**Sebastián Couto**
QA Engineer | SDET | Automation | Quality Engineering

Focused on test architecture, CI signal quality, meaningful automation, and practical feedback loops for modern engineering teams.
