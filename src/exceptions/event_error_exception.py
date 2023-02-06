class EventErrorException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class EventKeyError(EventErrorException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class EventK1ValeError(EventErrorException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class EventK2ValeError(EventErrorException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class EventSampleSizeError(EventErrorException):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
