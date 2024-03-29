import connexion
import six

from swagger_server.models.capture import Capture  # noqa: E501
from swagger_server.models.capture_update import CaptureUpdate  # noqa: E501
from swagger_server.models.trip import Trip  # noqa: E501
from swagger_server import util
from ..app import get_db_connection
from ..models.capture import Capture


def add_capture(body):  # noqa: E501
    if connexion.request.is_json:
        body = CaptureUpdate.from_dict(connexion.request.get_json())  # noqa: E501

    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            'INSERT into "Capture" ("tripID", "catchDate","speciesID", "quantity") VALUES (%s,%s, 2, %s) returning "captureID"',
            (body.trip, body.catch_date, body.quantity),
        )
        row = cur.fetchone()
        id = row[0]
        conn.commit()
        cur.close()

        cur = conn.cursor()
        cur.execute(
            'SELECT "captureID", "catchDate", "speciesID", "quantity" FROM "Capture" WHERE "captureID" = %s',
            (id,),
        )
        row = cur.fetchone()
        updated_capture = Capture(id=row[0], quantity=row[3])
        return updated_capture

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        cur.close()
        conn.close()

    return ""


def capture_id_get(id):  # noqa: E501
    """Get a capture by ID

     # noqa: E501

    :param id: ID of the capture to get
    :type id: int

    :rtype: Capture
    """
    return "do some magic!"


def capture_id_put(body, id):  # noqa: E501
    """Update an existing capture

     # noqa: E501

    :param body:
    :type body: dict | bytes
    :param id:
    :type id: int

    :rtype: CaptureUpdate
    """
    if connexion.request.is_json:
        body = CaptureUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"


def find_by_catch_date(catch_date=None):  # noqa: E501
    """Finds Captures by Catch Date

     # noqa: E501

    :param catch_date: CatchDate values that need to be considered for filter
    :type catch_date: str

    :rtype: List[Capture]
    """
    catch_date = util.deserialize_date(catch_date)
    return "do some magic!"


def get_all_captures():  # noqa: E501
    conn = get_db_connection()
    captures = []
    try:
        cur = conn.cursor()
        cur.execute(
            'SELECT "captureID", "catchDate", "speciesID", "quantity" from "Capture"'
        )
        for row in cur:
            c = Capture(id=row[0], quantity=row[3])
            captures.append(c)

    except:
        conn.rollback()
    finally:
        cur.close()
        conn.close()

    return captures


def update_capture(body):  # noqa: E501
    """Update an existing capture

    Update an existing capture by Id # noqa: E501

    :param body: Update an existent capture in the store
    :type body: dict | bytes

    :rtype: Capture
    """
    if connexion.request.is_json:
        body = Capture.from_dict(connexion.request.get_json())  # noqa: E501
    return "do some magic!"


def update_capture(id, trip, catch_date, quantity):  # noqa: E501

    if connexion.request.is_json:
        trip = Trip.from_dict(connexion.request.get_json())  # noqa: E501
    catch_date = util.deserialize_date(catch_date)
    return "do some magic!"
