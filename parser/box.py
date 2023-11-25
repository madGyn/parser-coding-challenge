"""
Is a simply class to represent and store the data from the file.
"""


class Box:
    length: int
    """
    The length of the box: obtained from the first four bytes 
    """

    name: str
    """
    The name of the box: obtained from the bytes 4 - 7
    """

    data: bytes
    """
    The data of the box
    """

    children: list
    """
    The children of the box
    """

    def __init__(self, length: int, name: str, data: bytes):
        self.length = length
        self.name = name
        self.data = data
        self.children = []
