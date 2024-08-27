from Requests.BaseRequest import BaseRequest


class WildberriesRequest(BaseRequest):
    def __init__(self, token, id) -> None:
        super().__init__()
        self.id = id
        self._requests.post()