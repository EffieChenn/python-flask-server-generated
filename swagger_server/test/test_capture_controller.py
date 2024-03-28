# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.capture import Capture  # noqa: E501
from swagger_server.models.capture_update import CaptureUpdate  # noqa: E501
from swagger_server.models.trip import Trip  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCaptureController(BaseTestCase):
    """CaptureController integration test stubs"""

    def test_add_capture(self):
        """Test case for add_capture

        Add a new capture
        """
        body = Capture()
        data = dict(id=789,
                    trip=Trip(),
                    catch_date='2013-10-20',
                    quantity=56)
        response = self.client.open(
            '/api/capture',
            method='POST',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_capture_id_get(self):
        """Test case for capture_id_get

        Get a capture by ID
        """
        response = self.client.open(
            '/api/capture/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_capture_id_put(self):
        """Test case for capture_id_put

        Update an existing capture
        """
        body = CaptureUpdate()
        response = self.client.open(
            '/api/capture/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_by_catch_date(self):
        """Test case for find_by_catch_date

        Finds Captures by Catch Date
        """
        query_string = [('catch_date', '2013-10-20')]
        response = self.client.open(
            '/api/capture/findByCatchDate',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_captures(self):
        """Test case for get_all_captures

        Get all captures
        """
        response = self.client.open(
            '/api/capture',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_capture(self):
        """Test case for update_capture

        Update an existing capture
        """
        body = Capture()
        data = dict(id=789,
                    trip=Trip(),
                    catch_date='2013-10-20',
                    quantity=56)
        response = self.client.open(
            '/api/capture',
            method='PUT',
            data=json.dumps(body),
            data=data,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
