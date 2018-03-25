import random
import typing

from apistar.backends.sqlalchemy_backend import Session
from apistar.http import Response

from .models import Fortune
from .serializers import FortuneSerializer


def get_random_fortune(session: Session):
    """
    Get a random fortune from the queryset.
    """
    
    queryset = session.query(Fortune).all()
    record = random.choice(queryset)
    data = FortuneSerializer(record)
    
    return Response(data, status=201)

def create_fortune(session: Session, message: str):
    """
    Create a new fortune.
    """
    
    fortune = Fortune(message=message)
    session.add(fortune)
    session.flush()  # can also use .commit() here
    
    return {'id': fortune.id, 'message': fortune.message}

def get_fortune(session: Session, uuid: str):
    """
    Get a specific fortune, given a specific UUID.
    """
    
    if uuid is None:
        data = {'message': 'Please select a message.'}
        return Response(data, status=404)
    
    queryset = session.query(Fortune).filter(Fortune.uuid==uuid)
    record = queryset.first()
    
    return FortuneSerializer(record)

def update_fortune(session: Session, uuid: str, message: str):
    """
    Update a specific fortune, given a specific UUID.
    """
    
    if uuid is None:
        data = {'message': 'Please select a message.'}
        return Response(data, status=404)
    
    if not message:
        data = {'message': 'Please set a new message.'}
        return Response(data, status=400)
    
    queryset = session.query(Fortune).filter(Fortune.uuid==uuid)
    record = queryset.first()
    record.message = message
    
    session.commit()
    
    queryset = session.query(Fortune).filter(Fortune.uuid==uuid)
    record = queryset.first()
    
    return FortuneSerializer(record)

def list_fortunes(session: Session) -> typing.List[FortuneSerializer]:
    """
    List all available fortunes.
    """
    
    queryset = session.query(Fortune).all()
    
    return [FortuneSerializer(record) for record in queryset]
