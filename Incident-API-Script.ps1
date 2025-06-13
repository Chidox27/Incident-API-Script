$apiUrl = "https://jsonplaceholder.typicode.com/posts"
$response = Invoke-RestMethod -Uri $apiUrl -Method Get
$response[0..4] | ForEach-Object { Write-Output "Incident Details $($_.ID): $($_.TITLE)" }