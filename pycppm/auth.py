#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

class CPPMAuth():
    """
    This class requests and stores an authentication cookie for CPPM
    Switch Software.
    """
    def __init__(self, cppmip, username, password, client_id, client_secret):
        url_login = "https://" + cppmip + "/api/oauth"
        grant_type = "password"
        version = "v1"
        payload_login = '{\"grant_type\": \"password\", \"username\": \"' + username + '\", \"password\": \"' + password + '\", \"client_id\": \"' + client_id + '", \"client_secret\": \"' + client_secret + '\"}'
        print("URL: ", url_login)
        print("payload: ", payload_login)
        headers = {'Content-Type': 'application/json'}
        get_access_token = requests.post(url_login, data=payload_login, headers=headers)
        if get_access_token.status_code != 200:
            #print(vars(get_access_token))
            print('Status:', get_access_token.status_code, 'Headers:', get_access_token.headers,
                  'Error Response:', get_access_token.reason)
            exit()
        access_token = get_access_token.json()['access_token']
        expires_in = get_access_token.json()['expires_in']
        refresh_token = get_access_token.json()['refresh_token']
        self.access_token = access_token
        self.ipaddr = cppmip
        self.version = version
        self.client_id = client_id
        self.client_secret = client_secret
        self.expires_in = expires_in
        self.refresh_token = refresh_token


    def logout(self):
        url_login = "http://" + self.ipaddr + "/rest/v1/login-sessions"
        headers = {'access_token': self.access_token}
        r = requests.delete(url_login, headers=headers)
        return r.status_code
