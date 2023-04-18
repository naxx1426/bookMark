import re,json

from django.shortcuts import redirect
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from it_drf_utils.api_view import ViewSetPlus, APIViewPlus
from it_drf_utils.exception import ValidationException
from it_drf_utils.mapping import post_mapping, get_mapping
from it_drf_utils.response import Response
from it_drf_utils.response_status import ResponseStatus
from it_drf_utils.exception import ValidationException

from django.http import HttpResponseRedirect

from bookmark.serializers import BookMarkSerializer, NewBookMarkSerializer,CategorySerializer
from bookmark.models import Bookmark,Category
from .error import MyResponseStatus
from rest_framework.decorators import action

#TODO 每个接口加用户验证
class BookMarkView(ViewSetPlus):
    base_url_name = "bookmark"
    base_url_path = "bookmark"

    @get_mapping(value="", detail=True)
    def index(self, request, pk, *args, **kwargs):
        cate_data = Category.objects.filter(user__username=pk)
        cate_serializer = CategorySerializer(cate_data, many=True)
        if cate_data.exists():
            _data = cate_serializer.data
            for i in _data:
                bookmark_data = Bookmark.objects.filter(user__username=pk,category=i.get("id"))[:9]
                serializer = BookMarkSerializer(bookmark_data, many=True)
                i["data"] = serializer.data
        return Response(ResponseStatus.OK, cate_serializer.data)

    @post_mapping(value="new", detail=True)
    def new(self, request, pk, *args, **kwargs):
        bookmark_data = Bookmark.objects.filter(user__username=pk)
        if not bookmark_data.exists():
            raise ValidationException(ResponseStatus.USER_NOT_EXIST)
        data = request.data
        data["user"] = 1
        if not isinstance(data.get("category"), int):
            data["category"] = None
        serializer = NewBookMarkSerializer(data=data)
        if not serializer.is_valid():
            raise ValidationException(ResponseStatus.USER_NOT_EXIST)
        serializer.save()

        return Response(ResponseStatus.OK)

    @post_mapping(value="edit", detail=True)
    def edit(self, request, pk, *args, **kwargs):
        data = request.data
        data["user"] = 1
        bm_id = data["id"]

        #TODO 序列化器验证

        bookmark_data = Bookmark.objects.filter(user__username=pk,id=bm_id)
        if not bookmark_data.exists():
            raise ValidationException(ResponseStatus.UB_NOT_EXIST)

        bookmark_data.update(name=data.get("name"), url=data.get("url"), introduction=data.get("introduction"),
                             icon=data.get("icon"), category_id=data.get("category"))
        return Response(ResponseStatus.OK)

    @post_mapping(value="search", detail=True)
    def search(self, request, pk, *args, **kwargs):
        data = request.data
        s = data.get("s")
        cate = request.query_params.get("category")
        bookmark_data = Bookmark.objects.filter(user__username=pk, category_id=cate,name__contains=s)
        serializer = BookMarkSerializer(bookmark_data,many=True)
        return Response(ResponseStatus.OK,serializer.data)

    @post_mapping(value="delete", detail=True)
    def delete(self, request, pk, *args, **kwargs):
        return Response(ResponseStatus.OK,)




    def default(request, *args, **kwargs):
        bookmark_data = Bookmark.objects.filter(isRecommond=1)
        serializer = BookMarkSerializer(bookmark_data, many=True)
        return Response(ResponseStatus.OK, serializer.data)




class MarkView(APIViewPlus):
    """链接计数"""
    base_url_name = "mark"
    base_url_path = "mark/go"

    def get(self, request, *args, **kwargs):
        data = request.query_params
        relax = "(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?"
        link = data.get("url")
        bookmark_id = data.get("id")
        if not isinstance(link, str) or isinstance(bookmark_id, int):
            raise ValidationException(ResponseStatus.BOOKMARK_NOT_EXIST)
        if not isinstance(re.match(relax, link), re.Match):
            link = "http://" + link

        bm = Bookmark.objects.filter(id=bookmark_id)
        if not bm.exists():
            raise ValidationException(ResponseStatus.BOOKMARK_NOT_EXIST)

        _bm = bm.first()
        _bm.access_number += 1
        _bm.save()

        return redirect(link)
