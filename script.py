import cgi 
import requests
import json
from simple_salesforce import Salesforce

consumer_key = 'ENTER KEY HERE'
consumer_secret = 'ENTER SECRET HERE'
request_token_url = 'https://login.salesforce.com/services/oauth2/token'
access_token_url = 'https://login.salesforce.com/services/oauth2/token'
redirect_url = ''
authorize_url = 'https://login.salesforce.com/services/oauth2/authorize' #?response_type=token&client_id='+consumer_key+'&redirect_uri='+redirect_uri

query = cgi.FieldStorage()
req = None

if 'login' in query:
    print "Location: https://login.salesforce.com/services/oauth2/authorize?response_type=code&client_id="+consumer_key+"&redirect_uri="+redirect_uri
    print

if 'code' in query:
    code = query.getvalue('code')

    data = {
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': code,
            'client_id' : consumer_key,
            'client_secret' : consumer_secret
    }
    headers = {
            'content-type': 'application/x-www-form-urlencoded'
    }
    req = requests.post(access_token_url, data=data,headers=headers)
    response = req.json()
    sf = Salesforce(instance_url=response['instance_url'], session_id=response['access_token'])
    records = sf.query("SELECT Id, Name, Email FROM Contact")
    records = records['records']

# Print the web page
print "Content-type: text/html"
print

print "<html><body>"
print "<h1>SELECT Id, Name, Email FROM Contact</h1>"

print "<table>"
print "<tr><td><b>Name</b></td><td><b>Email</b></td></tr>"
for record in records:
    print "<tr><td>"+record['Name']+"</td><td>"+record['Email']+"</td></tr>"

print "</table>"

print "</body></html>"