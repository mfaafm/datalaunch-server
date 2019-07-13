from datetime import datetime


def serialize_datetime(d):
    return {k: v.isoformat() if isinstance(v, datetime) else v for k, v in d.items()}
