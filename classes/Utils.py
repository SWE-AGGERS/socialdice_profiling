import requests

from classes.Errors import UserException, StoriesException
from classes.Stories import Stories
from classes.User import User

ENDPOINT_USER = 'http://0.0.0.0:5001/user/'

ENDPOINT_STORIES = 'http://0.0.0.0:5001/stories/'


def getStories(id:int):
    req = requests.get(url=ENDPOINT_STORIES+str(id))
    if req.status_code != 200:
        return Stories(None)

    stories: Stories = Stories(req.data)

    return stories


def getUser(id: int):
    req = requests.get(url=ENDPOINT_USER + str(id))
    if req.status_code != 200:
        raise UserException()
    u: User = User(req.data)

    return u
