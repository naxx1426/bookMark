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





