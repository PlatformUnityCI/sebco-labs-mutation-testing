````markdown
# sebco-labs-mutation-testing

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

The core logic lives under:

- `lib_core/time_utils/get_periods.py`
- `lib_core/time_utils/date_utils.py`
- `lib_core/time_utils/schedule_time.py`

The main business rule validates the expected monthly periods returned from an account creation date, including date-based behavior such as:

- when the current day is **5 or later**, the latest valid period should correspond to the **previous month**
- when the current day is **before the 5th**, the latest valid period should correspond to **two months back**
- the API-style response should return **up to 12 periods**

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
- billing/reporting periods
- boundary-driven business rules
- CI feedback quality

---

## Tech stack

- Python
- `pytest`
- `mutmut`
- `python-dateutil`
- GitHub Actions

---

## Repository structure

```text
.
├── .github/
│   └── workflows/
│       ├── pipeline.yml
│       ├── pr-governance.yml
│       └── release.yml
├── doc/
├── lib_core/
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
└── README.md
````

---

## Current test scope

The current suite covers both response-level and functional validation.

### Response-oriented validation

* validates the returned `accountCreatedDate`
* validates the generated `periodList`
* validates returned length depending on account age
* validates descending order and expected title/month/year values

### Functional rules

* includes previous month when the current day is `>= 5`
* skips previous month when the current day is `< 5`
* prevents current month from appearing when it should not
* enforces the expected month/title/year for the first returned item

---

## Mutation scope

Mutation testing is currently configured in `pyproject.toml` to target:

```toml
[tool.mutmut]
paths_to_mutate = ["lib_core/time_utils"]
tests_dir = ["tests"]
runner = "python -m pytest -m regression -q"
do_not_mutate = ["__init__.py"]
```

This means the mutation analysis focuses on the time and period calculation logic rather than mutating the whole repository.

---

## How to run locally

## 1) Create and activate a virtual environment

### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## 2) Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 3) Run the regression tests

```bash
pytest -m regression
```

## 4) Run mutation testing

```bash
mutmut run
```

## 5) Inspect results

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

This is good.
It means the suite is protecting the intended behavior.

### Survived mutant

A mutation changed the logic, but the tests still passed.

This is the main learning signal.
It usually means one of these is true:

* the assertion is too weak
* the wrong thing is being asserted
* a boundary case is missing
* the test executes the code but does not verify the business meaning

### Suspicious / timeout / unsupported cases

These should be reviewed separately depending on the mutation and runtime context.

---

## CI integration

This repository also includes GitHub Actions workflows that go beyond local experimentation.

The pipeline currently:

* runs the `pytest` regression suite
* publishes test results
* runs mutation testing
* collects mutation artifacts
* extracts surviving mutant IDs
* generates per-mutant details and diffs
* calculates mutation score
* posts a mutation summary comment on pull requests

This helps turn mutation testing into a reusable CI feedback signal instead of leaving it as a purely local tool.

---

## Live CI example (mutation run)

You can explore a real mutation testing execution from this repository here:

👉 https://github.com/PlatformUnityCI/sebco-labs-mutation-testing/actions/runs/23945300593

This run includes:

- executed test suite with mutation scope
- mutation results and score
- surviving mutants
- generated artifacts with detailed diffs

Suggested review flow:

1. Open the run link above
2. Navigate to the mutation job
3. Inspect generated artifacts:
   - `mutmut-results.txt`
   - `mutmut-show.txt`
   - `mutmut-diffs.txt`
4. Review surviving mutants and understand why they were not detected

This demonstrates how mutation testing moves from a local experiment to a **CI-level quality signal**.

---

## Mutation artifacts generated in CI

The workflow produces files such as:

* `mutmut-run.txt`
* `mutmut-results.txt`
* `mutmut-show.txt`
* `mutmut-diffs.txt`
* `surviving-mutants.txt`
* `mutation-score.txt`

These artifacts make it easier to:

* inspect what survived
* understand how the mutation changed the code
* decide whether to improve tests or accept the risk
* use mutation evidence in pull request reviews

---

## Example learning outcomes from this PoC

This project is useful for identifying situations like:

* a date rule is exercised but not truly verified
* a report boundary is asserted indirectly instead of explicitly
* a list length is validated, but the content semantics are still weak
* month/title/year combinations pass even though one business condition changed

That is exactly the kind of gap mutation testing is meant to expose.

---

## Why this matters for Quality Engineering

This repo reflects a broader testing principle:

> good automation is not only about running tests
> it is about producing trustworthy signals

For that reason, this PoC is not meant to be just a tooling exercise.

It is a practical step toward:

* stronger backend test design
* better CI signal quality
* more meaningful coverage discussions
* better pull request feedback
* safer refactoring of business logic

---

## Roadmap

Possible next steps for this lab:

* expand mutation scenarios across additional business rules
* harden assertions around edge dates and ordering behavior
* compare mutation score trends over time
* reuse this pattern in broader CI governance flows
* enrich PR feedback using mutation evidence as a first-class signal

---

## Who this is for

This repository is useful for people interested in:

* QA Engineering
* SDET practices
* backend automation
* CI quality signals
* mutation testing with Python
* contract and business-rule validation

---

## From execution to quality signal

This project is not only about running mutation testing.

The goal is to transform raw mutation output into a usable signal for engineering teams.

Instead of only generating reports, this approach enables:

- faster identification of weak assertions
- better pull request discussions based on evidence
- reduced noise compared to traditional CI signals
- more confidence when refactoring business logic

Mutation testing becomes valuable when it is **interpreted**, not only executed.

---

## Author

**Sebastián Couto**
QA Engineer | SDET | Automation | Quality Engineering

Focused on test architecture, CI signal quality, meaningful automation, and practical feedback loops for modern engineering teams.
