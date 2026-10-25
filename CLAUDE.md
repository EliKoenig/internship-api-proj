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
- `pytest.ini` sets `pythonpath = .` so plain `pytest` (used in CI) can import the app modules.
- `main` is branch-protected: the **test** check must pass before a PR can merge.
- Claude runs locally in this repo. Eli writes and commits the code; Claude reviews diffs (`git diff main...HEAD`) and runs tests.

## Roadmap at a glance

| Phase | Focus | Status |
|---|---|---|
| 1 | FastAPI CRUD, Pydantic validation, Swagger | ✅ Done |
| 1.5 | pytest suite + GitHub Actions CI | ✅ Done |
| 2 | Database + frontend prep: Postgres in Docker, migrations, CORS, status field, filters | 🟡 In progress |
| 2.5 | Frontend MVP: React + TS (Vite), list applications, add forms, API URL from env | ⬜ |
| 3 | Deploy early: API + managed Postgres, static frontend, health check, logs | ⬜ |
| 4 | Frontend features: status dropdown, filters, edit/delete, notes, styling | ⬜ |
| 5 | Auth: registration, login, hashing, JWT, user-owned data | ⬜ |
| 6 | Optional AI feature: paste a job posting, LLM pre-fills the form | ⬜ |
| 7 | Polish: README with live link, diagram, demo GIF, AI_USAGE.md | ⬜ |

## Current state of the code (late October 2026)

- **No persistence.** Routes store data in Python lists in `database.py` (`companies`, `applications`, `counters`).
  Everything is lost when the server restarts.
- `database.py` creates a SQLAlchemy engine (`sqlite:///internship_tracker.db`), `SessionLocal`, and `Base`, but **nothing uses them**.
  No tables are ever created.
- `models.py` defines SQLAlchemy `Company` and `Application` models (FK `company_id`), **not used by any route**.
  `Application.status` there is a plain `str`.
- **Status field:** exists at the API level. `schemas.py` has `ApplicationStatus(str, Enum)` with
  `Applied`, `Interviewing`, `Offer`, `Rejected`; invalid values get a 422. (The roadmap says "Interview"; the code says "Interviewing".)
- No Postgres driver, Alembic, or Docker Compose yet. No response models (routes return dicts).
- `POST` routes return 201. Applications must reference an existing company (400 otherwise).
  Deleting a company that still has applications returns 409 (Eli chose blocking over cascade delete).
- 16 tests on `feature/cors`, 14 on `main`.

## Where we are right now

**In progress: CORS (Phase 2, step 3)** on branch `feature/cors` (pushed, not merged).
- Done: `CORSMiddleware` in `main.py` allowing `http://localhost:5173` (Vite dev server), methods and headers `*`;
  tests `test_cors_allows_frontend_origin` and `test_cors_blocks_unkown_origin`.
- Review fixes still to make before merging:
  1. `test_cors_blocks_unkown_origin` asserts `headers.get(...) != "http://evilguy.com"`, which would still pass if
     `allow_origins` became `["*"]`. Change to `assert "access-control-allow-origin" not in response.headers`.
  2. Rename `unkown` → `unknown`.
  3. Move the `CORSMiddleware` import up next to `from fastapi import FastAPI`.
- Then: tests pass → push → PR → green check → merge.

Eli's understanding of why not `allow_origins=["*"]` (worth reinforcing): CORS is a browser rule, not access control;
it limits which websites can call the API from a visitor's browser. Matters once auth exists. Real protection is auth.

## Checklist (in order)

**Phase 2: database + frontend prep**
1. ~~Merge `feature/company-delete`~~ ✅ (PR #3)
2. ~~Add CLAUDE.md, ROADMAP.md, settings~~ ✅ (PR #4)
3. CORS ← **current**
4. Pick status values: `Interview` vs `Interviewing`, and whether to use lowercase values. Make code and `docs/ROADMAP.md` match.
   Eli's decision; the frontend's TS types will copy it.
5. Switch routes to SQLAlchemy on SQLite: `get_db` dependency (`connect_args={"check_same_thread": False}`), read schemas with
   `ConfigDict(from_attributes=True)` + `response_model=`, temporary `Base.metadata.create_all`, test DB via
   `app.dependency_overrides`, `*.db` in `.gitignore`. Companies first, then applications. Biggest step: go slowly.
6. Postgres via Docker Compose; `DATABASE_URL` from an env var; psycopg driver.
7. Alembic migrations (replace `create_all`).
8. Constraints/indexes: status as an Enum column, unique company name, `created_at`, index on `company_id`.
9. Filter endpoint: `GET /applications?status=...&company_id=...`.
10. Postgres service container in CI.

**Phase 2.5: frontend MVP** (can start after CORS merges, in parallel with 5–10)
11. Node LTS; `npm create vite@latest` (React + TypeScript) in `frontend/`.
12. API base URL from `VITE_API_URL`.
13. TS types matching `CompanyCreate`, `ApplicationCreate`, `ApplicationStatus`.
14. Applications list page with loading and error states.
15. Add-company and add-application forms.

**Anytime / small**
- Failure-case tests: 404 for GET/PATCH/DELETE missing company, 404 for GET missing application,
  400 for PATCH application with bad `company_id`, 422 for POST company without `name`.
- Start `AI_USAGE.md` (not created yet). Remind Eli.
- README: add the PowerShell activate command (`.\.venv\Scripts\Activate.ps1`) next to `activate.bat`.
- Move `ApplicationStatus` next to the application schemas; fix the `applicaiton` typo in a test name.

## Things Eli has tripped on (help quickly)

- Forgetting to activate the venv → "pytest is not recognized" / "No module named …". Fix: `.\.venv\Scripts\Activate.ps1`.
  Each computer needs its own venv (`python -m venv .venv` + `pip install -r requirements.txt`). VS Code's
  "Python: Select Interpreter" → `.venv` makes new terminals auto-activate.
- Committing before saving or without running tests. Encourage `git status` + `python -m pytest` before every commit.
- Pushing a new branch needs `git push -u origin <branch>`; "src refspec … does not match any" means the branch wasn't created.

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
