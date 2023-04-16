import json, os

from rest_framework import serializers

from bookmark.models import Bookmark
from django.conf import settings
from it_drf_utils.response import Response, ResponseStatus
from it_drf_utils.exception import ValidationException
from it_drf_utils.serializers import ITModelSerializer


class BookMarkSerializer(ITModelSerializer):
    class Meta:
        model = Bookmark
        exclude  = ["isRecommond", "access_time", "access_number", "user", "updated","created"]



class NewBookMarkSerializer(ITModelSerializer):
    class Meta:
        model = Bookmark
        exclude  = ["id","isRecommond", "access_time", "access_number", "user", "updated","created"]
        extra_kwargs = {
            "mark_name": {
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
                    "blank": "INTRODUCTION_REQUIRED_ERROR",
                    "required": "INTRODUCTION_REQUIRED_ERROR"
                }
            },
            "icon": {
                "error_messages": {
                    "invalid": "ICON_ERROR",
                    "blank": "ICON_REQUIRED_ERROR",
                    "required": "ICON_REQUIRED_ERROR"
                }
            },
            "introduction": {
                "error_messages": {
                    "invalid": "INTRODUCTION_ERROR",
                    "blank": "INTRODUCTION_REQUIRED_ERROR",
                    "required": "INTRODUCTION_REQUIRED_ERROR"
                }
            },
        }