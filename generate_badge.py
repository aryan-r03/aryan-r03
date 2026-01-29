import requests
import os

USERNAME = "aryan-r03"
TOKEN = os.environ["GITHUB_TOKEN"]

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github+json"
}

# User stats
user = requests.get(
    f"https://api.github.com/users/{USERNAME}",
    headers=headers
).json()

repos = requests.get(
    f"https://api.github.com/users/{USERNAME}/repos?per_page=100",
    headers=headers
).json()

public_repos = user["public_repos"]
followers = user["followers"]
stars = sum(r["stargazers_count"] for r in repos)

# Simple deterministic score
score = public_repos * 5 + followers * 4 + stars * 3

if score >= 300:
    grade = "S"
elif score >= 200:
    grade = "A+"
elif score >= 150:
    grade = "A"
elif score >= 100:
    grade = "B"
else:
    grade = "C"

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="280" height="40">
<rect width="280" height="40" rx="8" fill="#0f172a"/>
<text x="15" y="26" fill="#e5e7eb" font-size="15">GitHub Performance</text>
<text x="210" y="26" fill="#38bdf8" font-size="18">{grade}</text>
</svg>
"""

with open("grade.svg", "w") as f:
    f.write(svg)

print("Grade generated:", grade)
