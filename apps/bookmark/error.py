from enum import Enum
from it_drf_utils.response_status import ResponseStatus

class MyResponseStatus(Enum):


    @property
    def code(self):
        return self.value[0]

    @property
    def msg(self):
        return self.value[1]