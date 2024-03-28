import connexion
import six

from swagger_server.models.trip import Trip  # noqa: E501
from swagger_server.models.trip_update import TripUpdate  # noqa: E501
from swagger_server import util


def get_all_trips():  # noqa: E501
    """Get all trips

     # noqa: E501


    :rtype: List[Trip]
    """
    return 'do some magic!'


def trip_id_delete(id):  # noqa: E501
    """Delete a trip by ID

     # noqa: E501

    :param id: ID of the trip to delete
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def trip_id_get(id):  # noqa: E501
    """Get a trip by ID

     # noqa: E501

    :param id: ID of the trip to get
    :type id: int

    :rtype: Trip
    """
    return 'do some magic!'


def trip_id_put(body, id):  # noqa: E501
    """Update an existing trip

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: TripUpdate
    """
    if connexion.request.is_json:
        body = TripUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def trip_post(body):  # noqa: E501
    """Create a new trip

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Trip
    """
    if connexion.request.is_json:
        body = Trip.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
