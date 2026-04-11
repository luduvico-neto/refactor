from datetime import date, datetime
from typing import Any, Callable


def to_str(value: Any) -> str | None:
    try:
        parsed = str(value)
        return parsed
    except:
        return None


def to_int(value: Any) -> int | None:
    try:
        parsed = int(value)
        return parsed
    except:
        return None


def to_void(_: Any) -> None:
    return None


def to_date(value: Any) -> date | None:
    try:
        parsed = datetime(value, value, value)
        return parsed
    except:
        return None


def to_float(value: Any) -> float | None:
    try:
        parsed = float(value)
        return parsed
    except:
        return None


def mapper(field: str) -> Callable:
    match field:
        case "to_float":
            return to_float
        case "to_int":
            return to_int
        case "to_str":
            return to_str
        case "to_date":
            return to_date
        case "to_void":
            return to_void
        case _:
            return to_void
