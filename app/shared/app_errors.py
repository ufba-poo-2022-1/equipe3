class AppError(Exception):
    """All custom API exceptions"""

    def __init__(self, message, status_code=400, **kwargs):
        """Exception constructor"""
        Exception.__init__(self)

        self.message = message
        self.status_code = status_code
        self.kwargs = kwargs

    def to_dict(self):
        response_dict = dict()
        response_dict["message"] = self.message

        for key, value in self.kwargs.items():
            response_dict[key] = value

        return response_dict
