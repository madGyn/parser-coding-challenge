"""
Some useful functions to extract value from data
"""


def read_int_from_data(data, start, end, byteorder):
    return int.from_bytes(data[start:end], byteorder)


def read_string_from_data(data, start, end, encoding):
    return data[start:end].decode(encoding)
