#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json

import urllib3
import logging
import certifi
from error import (
    EosdNoResponse,
    HttpAPIError,
)

from urllib3.exceptions import (
    MaxRetryError,
    ReadTimeoutError,
    ProtocolError

)
from urllib.parse import urlparse

from itertools import cycle

logger = logging.getLogger(__name__)


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
    def _nodes(nodes):
        if type(nodes) == str:
            nodes = nodes.split(',')
        return [x.rstrip('/') for x in nodes]

    @staticmethod
    def _read_body(body):
        '''
            http method is post, need to specify the body params
        '''
        if type(body)  not in [dict, str, type(None)] :
            raise ValueError(
                'Request body is not a valid type %s' % type(body))
        if type(body) is dict:
            return json.dumps(body).encode('utf-8')
        return body

    def http_call(self, api, interface, body=None, _count=0, **kwargs):
        '''
        构造一个http connectionpool
        '''

        timeout = urllib3.Timeout(
            connect=kwargs.get('connect_timeout', 15),
            read=kwargs.get('timeout', 30))

        self.http = urllib3.poolmanager.PoolManager(
            retries=kwargs.get('http_retries', 10),
            timeout=timeout,
            headers={'Content-Type': 'application/json'},
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
        )

        url = f"{self.node_url}/{self.api_version}/{api}/{interface}"

        body = self._read_body(body)
        method = 'POST' if body else 'GET'

        print(url, method, body)
        try:
            response = self.http.urlopen(method, url, body)
        except (ReadTimeoutError,
                MaxRetryError,
                ProtocolError ) as e:
            raise e
            time.sleep(_count)
            self.next_node()
            logging.debug('switch to next node %s')
            return self.http_call(api, interface, boyd, _count = _count + 1)
        except Exception as e:
            extra = dict(err=e, url=url, body=body, methon=method)

            logging.info("Request error", extra=extra)

            raise e
        else:

            return self._return(response=response, body=body
            )

    @staticmethod
    def _return(response=None, body = None):
        """ parse the response and status code

        """
        if not response:
            raise EosdNoResponse(
                'eosd nodes have failed to respond, all retries exhausted.')

        result = response.data.decode('utf-8')
        if response.status !=200 or not result:
            extra = dict(result=result, response= response,request_body = body)

            logger.info("non ok response: %s" , response.status,extra=extra )
            raise HttpAPIError(response.status, result)

        #return json.dumps(result,indent=4)
        return result


#if __name__ == '__main__':
#    h = HttpRequest(["fullnode.eoshenzhen.io:8888", "fullnode.eoshenzhen.io:8888"])
#    print(h.http_call('chain', 'get_info'))