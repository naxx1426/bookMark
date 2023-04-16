from enum import Enum
from it_drf_utils.response_status import ResponseStatus

class MyResponseStatus(Enum):
    USER_NOT_EXIST = (41000,"用户不存在")
    BOOKMARK_NOT_EXIST = (41001,"书签不存在")

    @property
    def code(self):
        return self.value[0]

    @property
    def msg(self):
        return self.value[1]