# Internship Tracker: Full-Stack + Cloud Project Roadmap

A phased plan for building a resume-worthy full-stack project while learning practical software engineering skills.
Updated October 2026 to add a web frontend. (Converted from `internship_tracker_project_plan.pdf`; this file is the one to keep up to date.)

## Core idea

Don't try to learn every professional tool at once. Build one useful app in phases. Each phase should produce
a working artifact, a GitHub commit history, and a resume bullet.

## Project

**Internship Tracker**: a FastAPI backend plus a React + TypeScript web frontend for tracking companies, applications,
statuses, notes, contacts, and reminders. Repo: [github.com/EliKoenig/internship-api-proj](https://github.com/EliKoenig/internship-api-proj)

## Why the frontend is being added now

The original plan treated a frontend as an optional polish item. It was moved up in October 2026 for these reasons:

- **Target internship.** TELUS Digital (formerly WillowTree, headquartered in Charlottesville, VA) is hiring Software Engineer
  Interns for Summer 2027. The posting asks for a completed web or mobile project and experience in languages such as
  TypeScript or JavaScript, and prefers interest in using AI in development. A backend-only API does not fully meet that bar.
- **Full-stack shows product thinking.** TELUS Digital builds complete client products. One project that covers frontend,
  backend, database, and deployment shows how the pieces fit together.
- **A finished, live project.** A deployed app with a clickable link is stronger on a resume, LinkedIn, and in interviews
  than an in-progress API. It gives something concrete to demo.
- **Build in parallel, not last.** The API already works well enough for a frontend to call it. Backend gaps found while
  building the frontend (filters, a status field, etc.) get added as they come up.
- **Do not delay applying.** Applications go out with the current project; the live version is for interviews and later updates.

## Current status (October 2026)

- **Done:** Phase 1 (FastAPI CRUD for companies and applications, Pydantic validation, Swagger docs) and Phase 1.5
  (pytest suite running in GitHub Actions CI on every push and pull request).
- **Check first:** the repo has `database.py` and `models.py`. Confirm whether data currently persists (e.g., SQLite)
  before starting Phase 2.
- **Next up:** backend prep for the frontend, then the frontend MVP.

## Example endpoints

```
POST   /companies
GET    /companies
POST   /applications
GET    /applications
GET    /applications/{id}
PATCH  /applications/{id}
DELETE /applications/{id}
```

## Phased roadmap

| Phase | Focus | Build | Done when... |
|---|---|---|---|
| 1 (done) | Local REST API | FastAPI; request and response models; validation; Swagger/OpenAPI docs; GitHub repo. | The API runs locally with documented endpoints. |
| 1.5 (done) | Tests + GitHub Actions | Endpoint and unit tests; test data; CI workflow on pushes and pull requests. | A failing test blocks the build, and the README explains how to run tests. |
| 2 | Database + frontend prep | Persistent database (PostgreSQL in Docker); schema, constraints, migrations. Add CORS, an application status field (Applied, Interview, Offer, Rejected), and any filter endpoints the UI needs. | Data survives restarts and the browser can call the API. |
| 2.5 | Frontend MVP | React + TypeScript (Vite). Page that lists applications; form to add companies and applications; TypeScript types that match the Pydantic schemas; API base URL from an env variable. | You can view and add applications in the browser against the local API. |
| 3 | Deploy early | Backend on AWS App Runner (or Render/Railway to start) with managed Postgres; frontend on Vercel/Netlify (or S3 + CloudFront). Health check, logs, env-based config. Use demo data only until auth exists. | A public link works end to end and is at the top of the README. |
| 4 | Frontend features | Status dropdown, filters, edit and delete, notes, basic styling, loading and error states. | The app is pleasant to use for a real job search. |
| 5 | Authentication | Registration, login, password hashing, JWT, protected routes, user-owned data; login page in the frontend. | Each user can log in and only see their own applications. |
| 6 (optional) | AI feature | Paste a job posting; an LLM API extracts company, role, location, and deadline and pre-fills the form. User reviews before saving. API key stays on the backend. | Pasting a real posting fills the form correctly most of the time. |
| 7 | Polish | README with live link, architecture diagram, screenshots or demo GIF, AI_USAGE.md, resume bullets. | A recruiter can understand, try, and run the project from the repo. |

> **Priority:** phases 2, 2.5, and 3 matter most. A finished, deployed app without the AI feature beats a half-done one with it.

## Suggested stack

| Area | Recommendation | Why |
|---|---|---|
| Backend | Python + FastAPI | Beginner-friendly; OpenAPI/Swagger docs come almost for free. |
| Database | PostgreSQL | Widely used and excellent for learning relational modeling and SQL. |
| Local infrastructure | Docker Compose | Runs Postgres locally without installing everything directly. |
| Frontend | React + TypeScript (Vite) | Matches the TELUS Digital posting (TypeScript/JavaScript) and is the most common web stack. |
| Testing | pytest + FastAPI test client | Straightforward tests for endpoints and logic. Frontend tests (Vitest) are optional. |
| CI | GitHub Actions | Practical skill and an easy resume signal. |
| Cloud | AWS App Runner or ECS Fargate (API); Vercel/Netlify or S3 + CloudFront (frontend) | AWS supports the Cloud Practitioner goal. Render/Railway + Vercel are fine for a fast first deploy. |
| AI (optional) | An LLM API called from the backend | Covers the posting's preferred AI qualification with a useful feature. |

## What to learn in each phase

### Phase 1: Local REST API (done)
- HTTP methods, status codes, request and response bodies, headers.
- REST endpoint design and naming.
- Validation and error responses.
- OpenAPI/Swagger documentation.
- Small commits, frequent merges, clear commit messages.

### Phase 1.5: Tests + CI (done)
- Endpoint tests and unit tests.
- Running tests before merging.
- How CI catches regressions automatically.

### Phase 2: Database + frontend prep
- Relational modeling: users, companies, applications, notes, status history.
- Primary keys, foreign keys, unique and not-null constraints; indexes.
- Migrations and repeatable schema setup.
- SQL joins, filters, counts, grouping, latest-status lookups.
- CORS: why browsers block cross-origin requests and how to allow your frontend.

### Phase 2.5: Frontend
- React components, props, and state.
- Fetching data from an API; loading and error states.
- Controlled forms and client-side validation.
- TypeScript types and keeping them in sync with backend schemas.
- Environment variables for the API URL.

### Phase 3: Cloud
- Containerizing the API.
- Environment variables and secrets.
- Managed databases.
- Static frontend hosting and pointing it at a live API.
- Logs, health checks, and basic production troubleshooting.

### Phase 5: Auth
- Password hashing; never store plain-text passwords.
- JWT login flow; storing the token in the frontend.
- Protected routes and authorization checks.
- User-scoped data access.

### Phase 6: AI feature
- Calling an LLM API from the backend and keeping the API key secret.
- Asking for structured (JSON) output and validating it with Pydantic.
- Letting the user review AI output before it is saved.

## Optional certifications

The project is the centerpiece. A certification is a useful add-on if it gives structure and motivation.

| Certification | Usefulness | Recommendation |
|---|---|---|
| AWS Certified Cloud Practitioner | Good beginner cloud credential; not deeply technical by itself. | Good add-on during or after Phase 3, especially if deployed on AWS. |
| AWS Certified Developer - Associate | More developer-relevant, but significantly harder. | Stretch goal after the project is deployed. |
| GitHub Foundations | Useful for learning GitHub workflows. | Quick confidence-builder, not a centerpiece. |

## How to use AI coding tools

Notes for AI assistants (Claude Code, etc.) working on this repo: Eli is using this project to learn backend and
frontend development and must be able to explain every part of it in interviews. Explain concepts, review code, suggest
approaches, and help debug. Generate boilerplate, config, and tests when asked, but do not write whole features
unprompted. Prefer hints and step-by-step guidance on core logic so Eli writes it himself.

- **Good uses:** test generation, CI and deploy configuration, project setup, refactoring suggestions, README drafts, debugging help.
- Do not let AI build the whole project without understanding it. If you cannot explain a piece of code, rewrite it or study it until you can.
- Keep an `AI_USAGE.md` file explaining what tools were used, what they helped with, and how the output was verified.

## Resume bullets by milestone

| Milestone | Example resume bullet |
|---|---|
| Phase 1 + 1.5 | Built a REST API with FastAPI, Pydantic validation, and OpenAPI docs, with a pytest suite running in GitHub Actions CI. |
| Phase 2 | Replaced in-memory storage with PostgreSQL, designing a relational schema with migrations, constraints, and indexes. |
| Phase 2.5 + 4 | Built a React + TypeScript frontend to view, add, filter, and update applications through the REST API. |
| Phase 3 | Deployed the full-stack app to the cloud with managed PostgreSQL, environment-based configuration, health checks, and logs. |
| Phase 5 | Implemented JWT authentication, password hashing, protected routes, and user-scoped data access. |
| Phase 6 | Added an LLM-powered feature that extracts company, role, and deadline from pasted job postings into structured, validated data. |

**Bottom line:** A finished, documented, deployed full-stack project looks stronger than a beginner certification. The goal is
a GitHub repo, a live demo link, tests, clear docs, and the ability to explain the design tradeoffs in an interview.
