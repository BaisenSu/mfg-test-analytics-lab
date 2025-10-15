param(
  [string]$RepoName = "mfg-test-analytics-lab",
  [string]$Private = "true"
)

Write-Host "Setting up Python venv and installing deps..." -ForegroundColor Cyan
python -m venv .venv
if ($IsWindows) { .\.venv\Scripts\Activate.ps1 } else { . ./.venv/bin/activate }
python -m pip install --upgrade pip
pip install -r scripts/requirements.txt

Write-Host "Running schema checks..." -ForegroundColor Cyan
python scripts/check_schema.py

Write-Host "Initializing git repo..." -ForegroundColor Cyan
git init
git checkout -b main
git add .
git commit -m "init: scaffold + mock data + KQL + CI"

Write-Host "Creating remote repo via gh CLI..." -ForegroundColor Cyan
# Requires gh auth login
$visibility = if ($Private -eq "true") { "--private" } else { "--public" }
gh repo create $RepoName $visibility --source=. --remote=origin --push

Write-Host "Done. Repo pushed. You can open a PR by creating a branch and pushing changes."
