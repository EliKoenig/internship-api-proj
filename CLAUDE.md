# CLAUDE.md

Context for Claude working on this repo with Eli. Read this before doing anything. The full plan is in `docs/ROADMAP.md`.

## Who and why

Eli is a sophomore computer engineering student at Virginia Tech. This repo is the **Internship Tracker**: a FastAPI backend,
with a React + TypeScript frontend being added, built to learn full-stack development and to use as a portfolio piece.

**Why the frontend now, not last:** Eli is targeting the TELUS Digital Summer 2027 Software Engineer Intern role. The
posting asks for a completed web or mobile project in languages like TypeScript or JavaScript, and prefers experience
using AI in development. A deployed full-stack app fits that much better than a backend-only API. So the frontend is
built in parallel with the backend, and backend gaps (status field, filters, CORS) get added as the UI needs them.
**Priority:** phases 2, 2.5, and 3. A deployed app without the AI feature beats a half-done one with it.

## How to work with Eli (most important)

Eli is using this project to learn and must be able to **explain every part of it in interviews**.

- Explain concepts, review Eli's code, suggest approaches, and help debug.
- For **core logic** (routes, queries, components, state): give hints or step-by-step guidance so Eli writes it.
  Point to the line, name the concept, and show a syntax pattern if needed.
- **Boilerplate, config files (CI, Docker, deploy), and test scaffolding:** fine to write when Eli asks.
- **Don't write whole features** unless Eli asks.
- One small task at a time: explain why, then the steps, then let Eli do it.
- When something fails, help Eli read the error (file and line, expected vs. actual) rather than just fixing it.
- Keep changes small, with clear commit messages.
- Keep explanations short and plain. Define jargon the first time you use it.
- Remind Eli to keep `AI_USAGE.md` updated (what AI helped with and how its output was checked).

## Environment

- Windows, **PowerShell**, Python 3.14. Local repo: `C:\Users\EliFi\Documents\GitHub\internship-api-proj`
- Activate the venv: `.\.venv\Scripts\Activate.ps1` (the `.\` is required in PowerShell)
  - "No module named pytest/fastapi" almost always means the venv isn't active or packages aren't installed
    (`python -m pip install -r requirements.txt`).
  - If scripts are blocked: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
- Run the app: `python -m uvicorn main:app --reload`, then open http://127.0.0.1:8000/docs
- Run tests: `python -m pytest`
- CI: `.github/workflows/tests.yml` runs pytest on pushes and PRs to `main`.
- Cloud Claude sessions can read the GitHub repo but can't push to it. Eli pushes; Claude reviews the pushed branch.

## Roadmap at a glance

| Phase | Focus | Status |
|---|---|---|
| 1 | FastAPI CRUD, Pydantic validation, Swagger | ✅ Done |
| 1.5 | pytest suite + GitHub Actions CI | ✅ Done |
| 2 | Database + frontend prep: Postgres in Docker, migrations, CORS, status field, filters | ⬜ Next |
| 2.5 | Frontend MVP: React + TS (Vite), list applications, add forms, API URL from env | ⬜ |
| 3 | Deploy early: API + managed Postgres, static frontend, health check, logs | ⬜ |
| 4 | Frontend features: status dropdown, filters, edit/delete, notes, styling | ⬜ |
| 5 | Auth: registration, login, hashing, JWT, user-owned data | ⬜ |
| 6 | Optional AI feature: paste a job posting, LLM pre-fills the form | ⬜ |
| 7 | Polish: README with live link, diagram, demo GIF, AI_USAGE.md | ⬜ |

## Current state of the code (October 2026)

- **No persistence.** Routes store data in Python lists in `database.py` (`companies`, `applications`, `counters`).
  Everything is lost when the server restarts.
- `database.py` creates a SQLAlchemy engine (`sqlite:///internship_tracker.db`), `SessionLocal`, and `Base`, but **nothing uses them**.
  No tables are ever created.
- `models.py` defines SQLAlchemy `Company` and `Application` models (FK `company_id`), **not used by any route**.
  `Application.status` there is a plain `str`.
- **Status field:** exists at the API level. `schemas.py` has `ApplicationStatus(str, Enum)` with
  `Applied`, `Interviewing`, `Offer`, `Rejected`; invalid values get a 422. (The roadmap says "Interview"; the code says "Interviewing".)
- **No CORS** middleware in `main.py`.
- No Postgres driver, Alembic, or Docker Compose yet. No response models (routes return dicts).
- `POST` routes return 201. Applications must reference an existing company (400 otherwise).

## Code layout

- `main.py`: creates the app and includes both routers
- `company_routes.py`, `application_routes.py`: CRUD routes (in-memory lists)
- `schemas.py`: Pydantic request models + `ApplicationStatus` enum
- `database.py`: unused SQLAlchemy setup + the in-memory lists the routes actually use
- `models.py`: unused SQLAlchemy models
- `tests/conftest.py`: `client` fixture, autouse fixture that clears the lists, `existing_company` fixture
- `tests/test_api.py`: endpoint tests
- `docs/ROADMAP.md`: the full plan

## Git workflow

- Branch per task off `main` (`git checkout main && git pull && git checkout -b <name>`), small commits, PR to `main`.
- Always run `git status` and `python -m pytest` before committing.

## Commits
- Never add "Co-Authored-By", "Generated with Claude Code", or any AI attribution to commit messages or PR descriptions.
- Commits must use my git identity, not Claude's.
