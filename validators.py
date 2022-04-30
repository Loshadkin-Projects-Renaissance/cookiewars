
import re


def validate_name(name: str) -> bool:
    return re.match("[a-zA-Z0-9-_#=\.\,\/\[\]\<\>\?\^\!\}\{\']{2,18}", name)