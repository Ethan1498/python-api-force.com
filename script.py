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