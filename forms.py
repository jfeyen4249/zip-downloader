
import requests
import os
import zipfile


store = input("Enter Store Number: ")
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

# Enter the usename and password for your server if required.
basicAuthCredentials = ('username', 'password')

# Add the URL to the zip file your are downloading in URL
url = 'http://127.0.0.1'+ store + '.zip' 
r = requests.get(url, auth=basicAuthCredentials)
print(url)

with open('forms.zip', 'wb') as f:
    f.write(r.content)

# Making a new folder on the desktop to extract the zip file.
os.mkdir(desktop + '\\Important Forms')

# extracting the files out of the Zip file
zip_ref = zipfile.ZipFile('forms.zip', 'r')
zip_ref.extractall(desktop + '\\Important Forms')
zip_ref.close()