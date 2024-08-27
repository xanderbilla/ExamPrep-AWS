<powershell>
# Instati IIS
Install-WindowsFeature -Name Web-Server -IncludeManagementTools

# Start the IIS service
Start-Service -Name W3SVC

# Setup a basic HTML page
$webpage = "C:\inetpub\wwwroot\index.html"

@"
<!DOCTYPE html>
<html>
    <head>
        <title>Lab03</title>
    </head>
    <body>
        <h1>Lab03</h1>
        <p>This is a test page for Lab03</p>
    </body>
</html>
"@ | Out-File -FilePath $webpage

# Restart the IIS service
Restart-Service -Name W3SVC
</powershell>