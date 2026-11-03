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
- Settings at the top of `build.py`: `PREFIX` (GitHub Pages subpath), `BASE` (canonical/sitemap URL), `KOFI_URL`.

## Current task: move to Cloudflare
1. Buy the domain with Cloudflare Registrar (owner logs in himself; confirm the domain name and total price with him before paying; he enters payment details himself).
2. Cloudflare Pages: connect GitHub repo `intid85/parentright-korea`, production branch `main`, no build command, output directory `/`.
3. Add the custom domain in Pages.
4. In `build.py` set `PREFIX = ""` and `BASE = "https://<domain>"`, rebuild, push.
5. Remind the owner to change the Website field on his Ko-fi profile to the new domain.
6. Optionally keep GitHub Pages running or disable it once Cloudflare is live.
