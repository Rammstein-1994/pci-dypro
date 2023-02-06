# helper
from ..exceptions.event_error_exception import EventKeyError


EVENT_KEYS = set("sample_size", "k1", "k2")


def has_key(dict, key):
    return key in dict.keys()


def inspect_event_keys(event):
    for key in EVENT_KEYS:
        if not has_key(event, key):
            raise EventKeyError("Missing key: " + key)


def parse_event(event):
    inspect_event_keys(event)
    return event["sample_size"], event["k1"], event["k2"]
