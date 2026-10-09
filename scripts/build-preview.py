"""Package a GitHub project-page preview without changing Cloudflare source."""
from pathlib import Path
import os
import shutil

root = Path(__file__).resolve().parents[1]
source = root / "public"
output = root / "_site"
base = os.environ.get("PREVIEW_BASE", "/haohorizon-website/")
assert base.startswith("/") and base.endswith("/") and ".." not in base
if output.exists():
    for existing in output.rglob("*"):
        if existing.is_file():
            existing.unlink()
output.mkdir(exist_ok=True)
for path in source.rglob("*"):
    if not path.is_file():
        continue
    destination = output / path.relative_to(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".html":
        text = path.read_text(encoding="utf-8")
        for attribute in ("href", "src"):
            text = text.replace(f'{attribute}="/', f'{attribute}="{base}')
        destination.write_text(text, encoding="utf-8")
    elif path.suffix == ".css":
        text = path.read_text(encoding="utf-8").replace("url('/", f"url('{base}")
        destination.write_text(text, encoding="utf-8")
    else:
        shutil.copyfile(path, destination)
(output / ".nojekyll").touch()
print(f"Preview artifact prepared with base {base}")
