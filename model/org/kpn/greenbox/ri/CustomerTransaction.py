# -*- coding: utf-8 -*-

""" avro python class for file: CustomerTransaction """

import json
from model.helpers import default_json_serialize, todict
from typing import Union
from model.org.kpn.greenbox.ri.TransactionType import TransactionType
from model.org.kpn.greenbox.ri.Product import Product


class CustomerTransaction(object):

    schema = """
    {
        "namespace": "org.kpn.greenbox.ri",
        "name": "CustomerTransaction",
        "type": "record",
        "fields": [
            {
                "name": "transaction",
                "type": {
                    "name": "TransactionType",
                    "type": "enum",
                    "symbols": [
                        "created",
                        "updated",
                        "cancelled"
                    ],
                    "namespace": "org.kpn.greenbox.ri"
                }
            },
            {
                "name": "customerId",
                "type": "string"
            },
            {
                "name": "postalCode",
                "type": "string"
            },
            {
                "name": "houseNumber",
                "type": "int"
            },
            {
                "name": "timestamp",
                "type": "long"
            },
            {
                "name": "products",
                "type": {
                    "type": "array",
                    "items": {
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
                }
            }
        ]
    }
    """

    def __init__(self, obj: Union[str, dict, 'CustomerTransaction']) -> None:
        if isinstance(obj, str):
            obj = json.loads(obj)

        elif isinstance(obj, type(self)):
            obj = obj.__dict__

        elif not isinstance(obj, dict):
            raise TypeError(
                f"{type(obj)} is not in ('str', 'dict', 'CustomerTransaction')"
            )

        self.set_transaction(obj.get('transaction', None))

        self.set_customerId(obj.get('customerId', None))

        self.set_postalCode(obj.get('postalCode', None))

        self.set_houseNumber(obj.get('houseNumber', None))

        self.set_timestamp(obj.get('timestamp', None))

        self.set_products(obj.get('products', None))

    def dict(self):
        return todict(self)

    def set_transaction(self, values: TransactionType) -> None:

        self.transaction = TransactionType(values)

    def get_transaction(self) -> TransactionType:

        return self.transaction

    def set_customerId(self, value: str) -> None:

        if isinstance(value, str):
            self.customerId = value
        else:
            raise TypeError("field 'customerId' should be type str")

    def get_customerId(self) -> str:

        return self.customerId

    def set_postalCode(self, value: str) -> None:

        if isinstance(value, str):
            self.postalCode = value
        else:
            raise TypeError("field 'postalCode' should be type str")

    def get_postalCode(self) -> str:

        return self.postalCode

    def set_houseNumber(self, value: int) -> None:

        if isinstance(value, int):
            self.houseNumber = value
        else:
            raise TypeError("field 'houseNumber' should be type int")

    def get_houseNumber(self) -> int:

        return self.houseNumber

    def set_timestamp(self, value: int) -> None:

        if isinstance(value, int):
            self.timestamp = value
        else:
            raise TypeError("field 'timestamp' should be type int")

    def get_timestamp(self) -> int:

        return self.timestamp

    def set_products(self, values: list) -> None:

        self.products = []
        if isinstance(values, list):
            for element in values:
                self.products.append(Product(element))
        else:
            raise TypeError("Field 'products' should be type list")

    def get_products(self) -> list:
        return self.products

    def serialize(self) -> None:
        return json.dumps(self, default=default_json_serialize)
