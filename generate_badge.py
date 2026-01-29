import requests
import os

USERNAME = "aryan-r03"
TOKEN = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"token {TOKEN}"}

user = requests.get(
    f"https://api.github.com/users/{USERNAME}",
    headers=headers
).json()

events = requests.get(
    f"https://api.github.com/users/{USERNAME}/events",
    headers=headers
).json()

commits_30d = sum(
    1 for e in events if e["type"] == "PushEvent"
)

repos = user["public_repos"]
followers = user["followers"]

repos_data = requests.get(
    f"https://api.github.com/users/{USERNAME}/repos",
    headers=headers
).json()

stars = sum(repo["stargazers_count"] for repo in repos_data)

score = (
    commits_30d * 2
    + repos * 5
    + stars * 3
    + followers * 4
)

if score >= 400:
    grade = "S"
elif score >= 300:
    grade = "A+"
elif score >= 200:
    grade = "A"
elif score >= 100:
    grade = "B"
else:
    grade = "C"

svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" width="250" height="40">
  <rect width="250" height="40" rx="8" fill="#0f172a"/>
  <text x="15" y="26" fill="#e5e7eb" font-size="16">GitHub Grade</text>
  <text x="180" y="26" fill="#38bdf8" font-size="18">{grade}</text>
</svg>
"""

with open("grade.svg", "w") as f:
    f.write(svg)
