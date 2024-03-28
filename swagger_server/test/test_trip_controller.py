# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.trip import Trip  # noqa: E501
from swagger_server.models.trip_update import TripUpdate  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTripController(BaseTestCase):
    """TripController integration test stubs"""

    def test_get_all_trips(self):
        """Test case for get_all_trips

        Get all trips
        """
        response = self.client.open(
            '/api/trip',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_trip_id_delete(self):
        """Test case for trip_id_delete

        Delete a trip by ID
        """
        response = self.client.open(
            '/api/trip/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_trip_id_get(self):
        """Test case for trip_id_get

        Get a trip by ID
        """
        response = self.client.open(
            '/api/trip/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_trip_id_put(self):
        """Test case for trip_id_put

        Update an existing trip
        """
        body = TripUpdate()
        response = self.client.open(
            '/api/trip/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_trip_post(self):
        """Test case for trip_post

        Create a new trip
        """
        body = Trip()
        response = self.client.open(
            '/api/trip',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
