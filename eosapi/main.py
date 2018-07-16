#!/usr/bin/env python
from http_res import HttpRequest
class API(HttpRequest):
    def __init__(self, nodes = None, **kwargs):
        super().__init__(nodes=nodes, **kwargs)

    def get_info(self):
        body= dict()
        return self.http_call(
            api='chain',
            interface='get_info',
            body=body
        )



if __name__ == '__main__':
    nodes = API(['http://fullnode.eoshenzhen.io:8888'])
    print(nodes.get_info())