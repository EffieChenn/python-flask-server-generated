# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CaptureUpdate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, trip: int=None, catch_date: date=None, quantity: int=None):  # noqa: E501
        """CaptureUpdate - a model defined in Swagger

        :param id: The id of this CaptureUpdate.  # noqa: E501
        :type id: int
        :param trip: The trip of this CaptureUpdate.  # noqa: E501
        :type trip: int
        :param catch_date: The catch_date of this CaptureUpdate.  # noqa: E501
        :type catch_date: date
        :param quantity: The quantity of this CaptureUpdate.  # noqa: E501
        :type quantity: int
        """
        self.swagger_types = {
            'id': int,
            'trip': int,
            'catch_date': date,
            'quantity': int
        }

        self.attribute_map = {
            'id': 'id',
            'trip': 'trip',
            'catch_date': 'catchDate',
            'quantity': 'quantity'
        }
        self._id = id
        self._trip = trip
        self._catch_date = catch_date
        self._quantity = quantity

    @classmethod
    def from_dict(cls, dikt) -> 'CaptureUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The capture_update of this CaptureUpdate.  # noqa: E501
        :rtype: CaptureUpdate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this CaptureUpdate.


        :return: The id of this CaptureUpdate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this CaptureUpdate.


        :param id: The id of this CaptureUpdate.
        :type id: int
        """

        self._id = id

    @property
    def trip(self) -> int:
        """Gets the trip of this CaptureUpdate.


        :return: The trip of this CaptureUpdate.
        :rtype: int
        """
        return self._trip

    @trip.setter
    def trip(self, trip: int):
        """Sets the trip of this CaptureUpdate.


        :param trip: The trip of this CaptureUpdate.
        :type trip: int
        """
        if trip is None:
            raise ValueError("Invalid value for `trip`, must not be `None`")  # noqa: E501

        self._trip = trip

    @property
    def catch_date(self) -> date:
        """Gets the catch_date of this CaptureUpdate.


        :return: The catch_date of this CaptureUpdate.
        :rtype: date
        """
        return self._catch_date

    @catch_date.setter
    def catch_date(self, catch_date: date):
        """Sets the catch_date of this CaptureUpdate.


        :param catch_date: The catch_date of this CaptureUpdate.
        :type catch_date: date
        """
        if catch_date is None:
            raise ValueError("Invalid value for `catch_date`, must not be `None`")  # noqa: E501

        self._catch_date = catch_date

    @property
    def quantity(self) -> int:
        """Gets the quantity of this CaptureUpdate.


        :return: The quantity of this CaptureUpdate.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """Sets the quantity of this CaptureUpdate.


        :param quantity: The quantity of this CaptureUpdate.
        :type quantity: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity
