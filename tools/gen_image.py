"""Generate one illustration with Cloudflare Workers AI and save it as a small JPEG (800px wide).

Usage: python tools/gen_image.py "<prompt>" assets/guides/<slug>/<n>.jpg

Needs env vars CLOUDFLARE_AI_TOKEN (Workers AI token) and CLOUDFLARE_ACCOUNT_ID.
Never commit the token. Images must not show faces or readable text (see docs/guide-writing-rules.md).
"""
import base64, io, json, os, sys, urllib.request
from PIL import Image

MODEL = "@cf/black-forest-labs/flux-1-schnell"
STYLE = (" Flat editorial illustration, soft muted teal and warm beige palette, simple shapes, "
         "no people's faces, no text, no letters, no numbers, no logos, no writing on any object.")

def main():
    prompt, out = sys.argv[1], sys.argv[2]
    token = os.environ["CLOUDFLARE_AI_TOKEN"]
    account = os.environ["CLOUDFLARE_ACCOUNT_ID"]
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4/accounts/{account}/ai/run/{MODEL}",
        data=json.dumps({"prompt": prompt + STYLE, "steps": 6}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        res = json.load(r)
    if not res.get("success"):
        sys.exit(f"generation failed: {res.get('errors')}")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    img = Image.open(io.BytesIO(base64.b64decode(res["result"]["image"]))).convert("RGB")
    img.thumbnail((800, 800))
    img.save(out, "JPEG", quality=78, optimize=True)
    print("saved", out, os.path.getsize(out), "bytes")

if __name__ == "__main__":
    main()
