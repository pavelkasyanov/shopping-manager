import json
from functools import wraps, partial

from sqlalchemy.exc import SQLAlchemyError

from src.domain import Session


def transactional(func):
    session = Session()

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(session=session, *args, **kwargs)
            return res

        except SQLAlchemyError as e:
            session.rollback()

            common_message = json.dumps({
                'message': ''.join(e.args),
                'code': e.code
            })
            raise Exception(common_message)

        except Exception as e:
            session.rollback()

            common_message = json.dumps({
                'message': ''.join(e.args)
            })
            raise Exception(common_message)
        finally:
            session.expunge_all()
            session.close()

    return wrapper
