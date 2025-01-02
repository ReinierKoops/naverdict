from naverdic.constants import CONNECTION_ERROR_MESSAGE


class NaverdicConnectionError(Exception):
    """
    Exception raised when network is unconnected
    """

    def __init__(self):
        pass

    def __str__(self):
        return CONNECTION_ERROR_MESSAGE

    def __repr__(self):
        return CONNECTION_ERROR_MESSAGE
