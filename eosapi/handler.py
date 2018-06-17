#!/usr/bin/env python
# -*-coding:utf-8 -*-

from urllib.parse import urlparse
import httplib, urllib


class Modle(object):
    '''


    '''

    def __init__(self ,node, **kwargs):
        self.api_version=kwargs.get('api_version', 'v1')

        self.retry=kwargs.get('max_retries','10')
        self.http = ur


    def next_node(self):


    def set_node(self):

    def hostname(self):
        return urlparse()


    def exe(self, api, endpoint, body=None, _retry_=0):



    def _retrun(response = None, body=None):



if __name__ == '__main__':
