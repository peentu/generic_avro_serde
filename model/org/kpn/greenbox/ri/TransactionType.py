# -*- coding: utf-8 -*-

""" avro python class for file: TransactionType """

import json
from enum import Enum
from model.helpers import default_json_serialize, DefaultEnumMeta, todict


class TransactionType(Enum, metaclass=DefaultEnumMeta):

    schema = """
    {
        "name": "TransactionType",
        "type": "enum",
        "symbols": [
            "created",
            "updated",
            "cancelled"
        ],
        "namespace": "org.kpn.greenbox.ri"
    }
    """

    created = 'created'
    updated = 'updated'
    cancelled = 'cancelled'

    def encode(self):
        return self.name

    def serialize(self) -> None:
        return json.dumps(self, default=default_json_serialize)
