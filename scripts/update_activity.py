import json
import os
import urllib.request
from datetime import datetime, timezone

USER = os.environ.get("GH_USER", "zrong-me")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
README = "README.md"

headers = {"Accept": "application/vnd.github+json", "User-Agent": "ZRONG-profile-updater"}
if TOKEN:
    headers["Authorization"] = f"Bearer {TOKEN}"

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/events/public?per_page=30",
    headers=headers
)
try:
    with urllib.request.urlopen(req, timeout=25) as response:
        events = json.loads(response.read().decode("utf-8"))
except Exception as exc:
    raise SystemExit(f"Could not retrieve GitHub activity: {exc}")

rows = []
seen = set()
for event in events:
    repo = event.get("repo", {}).get("name", "")
    kind = event.get("type", "")
    created = event.get("created_at", "")
    if not repo or repo.lower() == f"{USER}/{USER}".lower():
        continue
    if kind not in {"PushEvent", "PullRequestEvent", "IssuesEvent", "ReleaseEvent", "CreateEvent", "ForkEvent"}:
        continue
    key = (repo, kind, created)
    if key in seen:
        continue
    seen.add(key)
    name = repo.split("/")[-1]
    url = f"https://github.com/{repo}"
    if kind == "PushEvent":
        count = event.get("payload", {}).get("size") or event.get("payload", {}).get("distinct_size") or 1
        label = f"⬆️ Pushed {count} commit(s)"
    elif kind == "PullRequestEvent":
        label = f"🔀 Pull request {event.get('payload', {}).get('action', 'updated')}"
    elif kind == "IssuesEvent":
        label = f"❕ Issue {event.get('payload', {}).get('action', 'updated')}"
    elif kind == "ReleaseEvent":
        label = "📦 Published a release"
    elif kind == "CreateEvent":
        label = f"✨ Created {event.get('payload', {}).get('ref_type', 'a resource')}"
    else:
        label = "🍴 Forked repository"
    try:
        date = datetime.fromisoformat(created.replace("Z", "+00:00")).astimezone(timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        date = "Recent"
    rows.append((created, f"| {date} | {label} | [`{name}`]({url}) |"))
    if len(rows) >= 8:
        break

if rows:
    body = [
        "| Date (UTC) | Activity | Repository |",
        "|---|---|---|",
        *[r[1] for r in rows]
    ]
else:
    body = ["<p align=\"center\"><i>No recent public activity was found.</i></p>"]

with open(README, "r", encoding="utf-8") as f:
    content = f.read()

start = "<!-- ACTIVITY:START -->"
end = "<!-- ACTIVITY:END -->"
if start not in content or end not in content:
    raise SystemExit("README activity markers were not found.")
before, rest = content.split(start, 1)
_, after = rest.split(end, 1)
new_content = before + start + "\n" + "\n".join(body) + "\n" + end + after
with open(README, "w", encoding="utf-8") as f:
    f.write(new_content)
