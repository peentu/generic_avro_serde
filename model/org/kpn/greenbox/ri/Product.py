# -*- coding: utf-8 -*-

""" avro python class for file: Product """

import json
from model.helpers import default_json_serialize, todict
from typing import Union


class Product(object):

    schema = """
    {
        "name": "Product",
        "type": "record",
        "fields": [
            {
                "name": "productId",
                "type": "string"
            },
            {
                "name": "name",
                "type": "string"
            },
            {
                "name": "number",
                "type": "int"
            }
        ],
        "namespace": "org.kpn.greenbox.ri"
    }
    """

    def __init__(self, obj: Union[str, dict, 'Product']) -> None:
        if isinstance(obj, str):
            obj = json.loads(obj)

        elif isinstance(obj, type(self)):
            obj = obj.__dict__

        elif not isinstance(obj, dict):
            raise TypeError(
                f"{type(obj)} is not in ('str', 'dict', 'Product')"
            )

        self.set_productId(obj.get('productId', None))

        self.set_name(obj.get('name', None))

        self.set_number(obj.get('number', None))

    def dict(self):
        return todict(self)

    def set_productId(self, value: str) -> None:

        if isinstance(value, str):
            self.productId = value
        else:
            raise TypeError("field 'productId' should be type str")

    def get_productId(self) -> str:

        return self.productId

    def set_name(self, value: str) -> None:

        if isinstance(value, str):
            self.name = value
        else:
            raise TypeError("field 'name' should be type str")

    def get_name(self) -> str:

        return self.name

    def set_number(self, value: int) -> None:

        if isinstance(value, int):
            self.number = value
        else:
            raise TypeError("field 'number' should be type int")

    def get_number(self) -> int:

        return self.number

    def serialize(self) -> None:
        return json.dumps(self, default=default_json_serialize)
