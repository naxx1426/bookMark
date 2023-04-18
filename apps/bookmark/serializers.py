import json, os

from rest_framework import serializers

from bookmark.models import Bookmark,Category
from django.conf import settings
from it_drf_utils.response import Response, ResponseStatus
from it_drf_utils.exception import ValidationException
from it_drf_utils.serializers import ITModelSerializer


class BookMarkSerializer(ITModelSerializer):
    #从数据库对象序列化用
    class Meta:
        model = Bookmark
        exclude  = ["isRecommond", "access_time", "access_number", "user", "updated","created"]

class CategorySerializer(ITModelSerializer):
    #从数据库对象序列化用
    class Meta:
        model = Category
        fields = "__all__"



class NewBookMarkSerializer(ITModelSerializer):
    #反序列化用
    class Meta:
        model = Bookmark
        exclude  = ["id","isRecommond",  "access_number", "updated","created"]
        extra_kwargs = {
            "name": {
                "error_messages": {
                    "invalid": "MARKNAME_ERROR",
                    "blank": "MARKNAME_REQUIRED_ERROR",
                    "required": "MARKNAME_REQUIRED_ERROR"
                }
            },
            "url": {
                "error_messages": {
                    "invalid": "URL_ERROR",
                    "blank": "URL_REQUIRED_ERROR",
                    "required": "URL_REQUIRED_ERROR"
                }
            },
            "introduction": {
                "error_messages": {
                    "invalid": "INTRODUCTION_ERROR",
                    "blank": "INTRODUCTION_ERROR",
                    "required": "INTRODUCTION_ERROR"
                }
            },
            "icon": {
                "error_messages": {
                    "invalid": "ICON_ERROR",
                    "blank": "ICON_ERROR",
                    "required": "ICON_ERROR"
                }
            },
            "category": {
                "error_messages": {
                    "invalid": "CATEGORY_ERROR",
                    "blank": "CATEGORY_ERROR",
                    "required": "CATEGORY_ERROR"
                }
            },
        }

class EditBookMarkSerializer(ITModelSerializer):
    #反序列化用
    class Meta:
        model = Bookmark
        exclude  = ["id","isRecommond",  "access_number", "updated","created"]
        extra_kwargs = {
            "name": {
                "error_messages": {
                    "invalid": "MARKNAME_ERROR",
                    "blank": "MARKNAME_REQUIRED_ERROR",
                    "required": "MARKNAME_REQUIRED_ERROR"
                }
            },
            "url": {
                "error_messages": {
                    "invalid": "URL_ERROR",
                    "blank": "URL_REQUIRED_ERROR",
                    "required": "URL_REQUIRED_ERROR"
                }
            },
            "introduction": {
                "error_messages": {
                    "invalid": "INTRODUCTION_ERROR",
                    "blank": "INTRODUCTION_ERROR",
                    "required": "INTRODUCTION_ERROR"
                }
            },
            "icon": {
                "error_messages": {
                    "invalid": "ICON_ERROR",
                    "blank": "ICON_ERROR",
                    "required": "ICON_ERROR"
                }
            },
            "category": {
                "error_messages": {
                    "invalid": "CATEGORY_ERROR",
                    "blank": "CATEGORY_ERROR",
                    "required": "CATEGORY_ERROR"
                }
            },
        }

