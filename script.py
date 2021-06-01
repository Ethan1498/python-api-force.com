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
