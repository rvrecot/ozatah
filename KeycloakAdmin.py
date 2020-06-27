import json
import requests
from builtins import isinstance
from typing import List, Iterable
from .connection import ConnectionManager
from .exceptions import raise_error_from_response, KeycloakGetError
from .keycloak_openid import KeycloakOpenID
from .urls_patterns import URL_ADMIN_CLIENT

class KeycloakAdmin:
    
    _server_url = None
    _username = None
    _password = None
    _realm_name = None
    _client_id = None

    def __init__(self, server_url, username=None, password=None, realm_name='master', client_id='admin-cli'):
        
        self.server_url = server_url
        self.username = username
        self.password = password
        self.realm_name = realm_name
        self.client_id = client_id
    
    def raw_delete(self, *args, **kwargs):
            r = self.connection.raw_delete(*args, **kwargs)
            if 'delete' in self.auto_refresh_token and r.status_code == 401:
                self.refresh_token()
                return self.connection.raw_delete(*args, **kwargs)
            return r
    
    def delete_client(self, client_id):
        params_path = {"realm-name": self.realm_name, "id": client_id}
        data_raw = self.raw_delete(URL_ADMIN_CLIENT.format(**params_path))
        return raise_error_from_response(data_raw, KeycloakGetError, expected_code=204)

    def create_realm(self, payload):
        data_raw = self.raw_post(URL_ADMIN_REALMS, data=json.dumps(payload))
        return raise_error_from_response(data_raw, KeycloakGetError, expected_code=201)
    
