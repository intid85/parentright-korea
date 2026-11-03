# Guide writing rules

Rules for every guide in `guides.py`, whether written by hand or by the scheduled task. The hard rules in `CLAUDE.md` also apply.

## Content
- One guide answers one real question a mother (or someone helping her) would search for. Take the next unpublished topic from `docs/guide-topics.md`.
- English, plain words, short sentences, mobile-friendly: short paragraphs, lists, 600-1,200 words.
- Every fact, law article, number, amount, phone number and date must be backed by a source in `sources`. Prefer official sources (law.go.kr, scourt.go.kr, government agencies, HCCH, embassies). Use news reports only for court cases.
- If a fact cannot be confirmed from a source in this run, leave it out. Never fill gaps from memory. Write "ask the agency" instead of guessing.
- Do not contradict the home page. If research shows the home page is wrong, fix the home page in `build.py` in the same run and say so in the commit message.
- Link to the 6 steps (`/#steps`) or `/find-help.html` where it helps.

## Never
- Names, photos, contact details or stories of any real private person.
- Recommending a specific lawyer or law firm, or any paid referral.
- Telling a reader what to do in her specific case (no legal advice). Describe options and where to ask.
- Ko-fi or donation links inside guides.
- Publishing or shaming fathers, or encouraging readers to do so.

## Images (5 per guide)
- Generate with `python tools/gen_image.py "<prompt>" assets/guides/<slug>/<n>.jpg` (n = 1..5). Needs env vars `CLOUDFLARE_AI_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`; never print or commit the token.
- Objects and places only: no faces, no people in focus, no children, no flags of a specific country, no courtroom drama.
- Avoid subjects that invite fake writing (documents, signs, screens with text). Good subjects: a phone face down, a closed folder, a calendar without numbers, a desk lamp, a cloud and a USB stick, a telephone headset, a padlock, a road or path, a plane window, a houseplant.
- Look at each generated image before using it. If it shows letters, faces or anything misleading, regenerate with a different subject.
- Every image gets a plain `alt` text and a one-line `figcaption` that adds information.

## Publishing
1. Add the guide dict at the end of `GUIDES` in `guides.py`, with `checked` = today.
2. Mark the topic done in `docs/guide-topics.md` with the date and slug.
3. Run `python build.py`, copy `site/*` (including `.nojekyll`) to the repo root, delete `site/`.
4. Check `guides/<slug>.html` exists and contains no `{{`.
5. Commit on `main` with a message ending in the Co-Authored-By line, push to `origin main`. Cloudflare Pages deploys automatically.
6. Wait about a minute and confirm `https://parentright.org/guides/<slug>.html` returns 200.
