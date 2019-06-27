#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:34:55 2019

@author: hans
"""

from bs4 import BeautifulSoup
import urllib3
import certifi

def body_texter(url):
    """
    input url and return teh text of the body
    """
    # create pool
    c=urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    # download website
    content = c.request('GET', url)
    # make soup
    soup = BeautifulSoup(content.data)
    # get text from body
    text = soup.body.get_text()
    
    return text

def write_file(text, file="output.txt"):
    """ write to file"""
    with open(file, 'w') as t:
        for line in text:
            line = line.replace('\n', ' ')
            line = line.replace('\t', ' ')
            t.write(line)
    return " {} written".format(file)

if __name__ == "__main__":
    url = input("website? ")
    file = input("File? ")
    
    text = body_texter(url)
    write_file(text, file)