import requests
import json

token_ep_url = 'http://localhost:8080/auth/realms/master/protocol/openid-connect/token'
payload = {
    'client_id': 'admin-cli',
    'grant_type': 'password',
    'username' : 'admin',
    'password': 'admin'
}
response = requests.post(token_ep_url, payload)
response_json = json.loads(response.content)
access_token = response_json['access_token']

realm_url ='http://localhost:8080/auth/admin/realms'
headers = {
    'content-type': 'application/json',
    'Authorization' : 'Bearer ' + access_token
}
realm_response = requests.get(realm_url, headers=headers)
for realm in json.loads(realm_response.content):
    print(realm["realm"])
    
#1 Human readable format von JSON
ReadableFormat = str(response_json).replace(', ','\n')
print(ReadableFormat)
###############################################

#2 Create a new Realm
keycloak_admin.create_realm(payload={"realm": "demo"}, skip_exists=False)
###############################################

#3 Add another redirect URI to one of the clients

###############################################

#4 Delete one of the clients
delete_client(client_id = "account-console")

###############################################

#5 Detect that one of the clients is missing and add it again.

###############################################
