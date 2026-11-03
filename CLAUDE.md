# CLAUDE.md

This repo is **ParentRight Korea**, a static information site (EN/VI/KO) helping mothers abroad pursue paternity acknowledgment, child support and Korean nationality for children of Korean fathers through official legal channels. The owner communicates in Korean; reply in Korean.

Read `docs/project-notes.md` first: it has the operating principles, legal research, monetization decisions and the open task list.

## Hard rules
- Never add features that publish or collect information about any individual (no name/photo fields, no boards, comments, uploads, or forms that send data).
- Never add paid lawyer referrals or per-case/success-fee partnerships (Korean Attorney-at-Law Act).
- Keep "general information, not legal advice" notices.
- No donation buttons on `find-help.html` or country pages.
- This repo is public: do not commit emails, addresses, account numbers, API tokens or other personal data.

## How the site is built
- Edit `build.py` only (pages are generated). Run `python3 build.py`, copy `site/*` (including `.nojekyll`) to the repo root, delete `site/`, commit.
- Settings at the top of `build.py`: `PREFIX` (URL subpath, `""` at the domain root), `BASE` (canonical/sitemap URL), `KOFI_URL`.

## Hosting
- Live at https://parentright.org on Cloudflare Pages (project `parentright-korea`, production branch `main`, no build command, output `/`). Every push to `main` deploys automatically.
- Domain bought on Cloudflare Registrar 2026-11-03. Remaining follow-ups are in `docs/project-notes.md`.
