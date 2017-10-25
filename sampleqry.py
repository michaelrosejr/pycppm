#!/usr/bin/env python3
import sys, json, requests, datetime, time, os, logging, yaml
import pprint

from pycppm import auth
import pycppm.session as session
import pycppm.endpoints as endpoints

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

grant_type = cfg['grant_type']
cppmip = cfg['cppmip']
username = cfg['username']
password = cfg['password']
client_id = cfg['client_id']
client_secret = cfg['client_secret']



login=0
if login == 1:
    tempauth = auth.CPPMAuth(cppmip, username, password, client_id, client_secret)
    #print(tempauth.access_token)
    tempsession = {}
    tempsession['access_token'] = tempauth.access_token
    tempsession['expires_in'] = tempauth.expires_in
    tempsession['refresh_token'] = tempauth.refresh_token
    with open("cppmtoken.json", "w") as f:
        json.dump(tempsession, f)


with open("cppmtoken.json") as tokenfile:
    token = json.load(tokenfile)


#print("access_token", token['access_token'])
#print(json.dumps(session.get_session))
# print(json.dumps((session.get_session(token))))
print(json.dumps((endpoints.get_insight_endpoints(token))))
