#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import logging
import gzip

import body as body
import urllib3
from urllib.parse import urlparse

from StringIO import StringIO
from itertools import cycle


class HttpRequest(object):
    """
    构造一个http 方法，创建httpconnection pool 并增加retry 功能
    """
    def __init__(self, nodes, **kwargs):
        self.api_version = kwargs.get('api_version', 'v1')
        self.nodes = cycle(self._nodes(nodes))
        self.node_url = ''
        self.next_node()

    def next_node(self):
        """
        if the node provided is not unusefull,the switch to the next node
        :return:
        """
        self.set_node(next(self.nodes))

    def set_node(self, node_url):
       self.node_url = node_url

    def hostname(self):
       return urlparse(self.node_url).hostname

    @staticmethod
    def _read_body(obj):
        using_gzip = obj.headers.get('Content-Encoding', '') == 'gzip'
        body = obj.read()
        if using_gzip:
            gzipper = gzip.GzipFile(fileobj=StringIO(body))
            fcontent = gzipper.read()
            gzipper.close()
            return fcontent
        return body


    def http_call(self, the url, methon, interface,  body= None, _retry=0):
        '''
        构造一个http connection连接池
        '''
        self.http = urllib3.poolmanager.PoolManager(
            num_pools=kwargs.get('num_pools', 50),
            maxsize=kwargs.get('maxsize', 10),
            block=kwargs.get('pool_block', False),
            retries=kwargs.get('http_retries', 10),
            timeout=timeout,
            headers={'Content-Type': 'application/json'},
            ca_certs=certifi.where(),
         )

        url = f"{self.node_url}/{self.api_version}/{api}/{interface}/"
        body = self._read_body(body)
    
        method = 'POST'  if body else 'GET'
        reponse = self.http.urlopen(method, url, body)

        return reponse
        '''
        except (MaxRetryError,
                ConnectionResetError,
                ReadTimeoutError,
                RemoteDisconnected,
                ProtocolError) as e:
        '''


    def _exec(self, api, interface, body=None, retry=0):
        '''
    
        确定执行的方法 eosd RPC
        :return:
        '''
        url = f"{self.node_url}/{self.api_version}/{api}/{interface}"


    def __return(self):
        '''

        返回的结果处理
        :return:
        '''

if __name__ ==  '__main__':
    h = HttpClient(["http://localhost:8888", "http://localhost:8899"])
    print(h.http_call('chain','get_block',{"block_num_or_id": 5}))