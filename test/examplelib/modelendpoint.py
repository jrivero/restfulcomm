# -*- coding: utf-8 -*-
"""Example endpoint for parameters persistence"""
from restfulcomm.http.jsonrequest import JsonRequest
from restfulcomm.http.superendpoint import Endpoint
from werkzeug.wrappers import Response


class ModelEndpoint(Endpoint):

    items = {
        1: 'John Doe',
        2: 'Michael Knight',
        3: 'Paco Pena'
    }

    @classmethod
    def PUT(cls, request: JsonRequest, **kwargs):
        item_id = int(kwargs['item_id'])
        if item_id not in cls.items:
            return Response('Not Found', status=404)
        cls.items[item_id] = request.data['name']
        return Response('No Content', status=204)

    @classmethod
    def GET(cls, request: JsonRequest, **kwargs):
        item_id = int(kwargs['item_id'])
        if item_id not in cls.items:
            return Response('Not Found', status=404)
        return Response(
            response=cls.items[item_id],
            content_type='text/plain'
        )

    @classmethod
    def _last_id(cls):
        keys = sorted(cls.items.keys())
        return int(keys[-1]) + 1

    @classmethod
    def POST(cls, request: JsonRequest, **kwargs):
        item_id = cls._last_id()
        cls.items[item_id] = request.data['name']
        return Response('CREATED', status=201)

    @classmethod
    def DELETE(cls, request, **kwargs):
        item_id = int(kwargs['item_id'])
        if item_id not in cls.items:
            return Response('Not Found', status=404)
        del cls.items[item_id]
        return Response('No Content', status=204)
