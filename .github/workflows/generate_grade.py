name: Update GitHub Grade

permissions:
  contents: write

on:
  schedule:
    - cron: "0 */6 * * *"
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run script
        run: |
          pip install requests
          python generate_grade.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Commit changes
        run: |
          git config user.name "github-actions"
          git config user.email "actions@github.com"
          git add grade.svg
          git commit -m "Update GitHub grade" || echo "No changes"
          git push
