#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json


def get_identiy_endpoints(access_token):
    """
    Function to get list of mac-addresses from Aruba OS switch
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return list of mac-addresses
    :rtype list
    """
    headers = {'Accept': "application/json", 'Authorization': "Bearer " + access_token['access_token']}
    url = "https://cppm.home.rozebud.com:443/api/endpoint?filter=%7B%7D&sort=%2Bid&offset=0&limit=25&calculate_count=false"
    try:
        r = requests.get(url, headers=headers)
        endpoints = json.loads(r.text)
        return endpoints
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_mactable: An Error has occured"

def get_insight_endpoints(access_token):
    """
    Function to get list of mac-addresses from Aruba OS switch
    :param auth:  AOSSAuth class object returned by pyarubaoss.auth
    :return list of mac-addresses
    :rtype list
    """
    headers = {'Accept': "application/json", 'Authorization': "Bearer " + access_token['access_token']}
    url = "https://cppm.home.rozebud.com:443/api/insight/endpoint/mac/5cf5da13f999"
    try:
        r = requests.get(url, headers=headers)
        endpoints = json.loads(r.text)
        return endpoints
    except requests.exceptions.RequestException as error:
        return "Error:\n" + str(error) + " get_mactable: An Error has occured"
