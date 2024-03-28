# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.season import Season  # noqa: F401,E501
from swagger_server.models.ship import Ship  # noqa: F401,E501
from swagger_server import util


class Trip(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, start_date: date=None, end_date: date=None, ship: Ship=None, season: Season=None):  # noqa: E501
        """Trip - a model defined in Swagger

        :param id: The id of this Trip.  # noqa: E501
        :type id: int
        :param start_date: The start_date of this Trip.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this Trip.  # noqa: E501
        :type end_date: date
        :param ship: The ship of this Trip.  # noqa: E501
        :type ship: Ship
        :param season: The season of this Trip.  # noqa: E501
        :type season: Season
        """
        self.swagger_types = {
            'id': int,
            'start_date': date,
            'end_date': date,
            'ship': Ship,
            'season': Season
        }

        self.attribute_map = {
            'id': 'id',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'ship': 'ship',
            'season': 'season'
        }
        self._id = id
        self._start_date = start_date
        self._end_date = end_date
        self._ship = ship
        self._season = season

    @classmethod
    def from_dict(cls, dikt) -> 'Trip':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The trip of this Trip.  # noqa: E501
        :rtype: Trip
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Trip.


        :return: The id of this Trip.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Trip.


        :param id: The id of this Trip.
        :type id: int
        """

        self._id = id

    @property
    def start_date(self) -> date:
        """Gets the start_date of this Trip.


        :return: The start_date of this Trip.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this Trip.


        :param start_date: The start_date of this Trip.
        :type start_date: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self) -> date:
        """Gets the end_date of this Trip.


        :return: The end_date of this Trip.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: date):
        """Sets the end_date of this Trip.


        :param end_date: The end_date of this Trip.
        :type end_date: date
        """
        if end_date is None:
            raise ValueError("Invalid value for `end_date`, must not be `None`")  # noqa: E501

        self._end_date = end_date

    @property
    def ship(self) -> Ship:
        """Gets the ship of this Trip.


        :return: The ship of this Trip.
        :rtype: Ship
        """
        return self._ship

    @ship.setter
    def ship(self, ship: Ship):
        """Sets the ship of this Trip.


        :param ship: The ship of this Trip.
        :type ship: Ship
        """

        self._ship = ship

    @property
    def season(self) -> Season:
        """Gets the season of this Trip.


        :return: The season of this Trip.
        :rtype: Season
        """
        return self._season

    @season.setter
    def season(self, season: Season):
        """Sets the season of this Trip.


        :param season: The season of this Trip.
        :type season: Season
        """

        self._season = season