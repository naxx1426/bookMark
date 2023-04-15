from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from it_drf_utils.api_view import ViewSetPlus, APIViewPlus
from it_drf_utils.exception import ValidationException
from it_drf_utils.mapping import post_mapping, get_mapping
from it_drf_utils.response import Response
from it_drf_utils.response_status import ResponseStatus


class BookMarkView(APIViewPlus):
    base_url_name = "bookmark"
    base_url_path = "bookmark/<str:username>"

    def get(self, request, username, *args, **kwargs):
        print(username)
        return Response(ResponseStatus.OK)

    def default(request, *args, **kwargs):

        return Response(ResponseStatus.OK)




