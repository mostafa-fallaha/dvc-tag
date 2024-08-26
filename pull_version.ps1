param (
    [string]$Tag
)

if (-not $Tag) {
    Write-Host "Usage: .\pull_version.ps1 <python_file> <tag>"
    exit 1
}

try {
    # Run the specified Python script with the commit message
    python commands.py $Tag
} catch {
    Write-Host "An error occurred: $($_.Exception.Message)"
    exit 1
}
