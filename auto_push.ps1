
Set-Location "C:\Users\Sharm\OneDrive\Desktop\TCS_nqt"

git add -A

$changes = git status --porcelain

if ($changes) {
    git commit -m "Daily coding update: $(Get-Date -Format 'yyyy-MM-dd')"

    if ($LASTEXITCODE -eq 0) {
        git push origin main
    }
}
