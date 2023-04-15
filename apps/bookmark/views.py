import re

from django.shortcuts import redirect
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from it_drf_utils.api_view import ViewSetPlus, APIViewPlus
from it_drf_utils.exception import ValidationException
from it_drf_utils.mapping import post_mapping, get_mapping
from it_drf_utils.response import Response
from it_drf_utils.response_status import ResponseStatus

from django.http import HttpResponseRedirect

from bookmark.serializers import BookMarkSerializer
from bookmark.models import Bookmark


class BookMarkView(APIViewPlus):
    base_url_name = "bookmark"
    base_url_path = "bookmark/<str:username>"

    def get(self, request, username, *args, **kwargs):
        print(username)
        bookmark_data = Bookmark.objects.filter(user__username=username)
        serializer = BookMarkSerializer(bookmark_data,many=True)
        return Response(ResponseStatus.OK,serializer.data)

    def default(request, *args, **kwargs):

        return Response(ResponseStatus.OK)



class MarkView(APIViewPlus):
    base_url_name = "mark"
    base_url_path = "mark/go"

    def get(self, request, *args, **kwargs):
        data = request.query_params
        relax = "(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?"
        link = data.get("url")
        if not isinstance(link,str):
            return Response(ResponseStatus.OK)
        if not isinstance(re.match(relax,link),re.Match):
            link = "http://" + link
        return redirect(link)


