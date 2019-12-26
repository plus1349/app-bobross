from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_401_UNAUTHORIZED


class NotAuthenticated(APIException):
    status_code = HTTP_401_UNAUTHORIZED
    default_detail = {'success': False, 'error': 'Not authorized.'}
