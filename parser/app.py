"""
The main class of the project.
Using a recursive function the metadata of the boxes are parsed into a list of elements of type `Box` class.
"""

import base64

from .box import Box as Box
from .helper import read_int_from_data, read_string_from_data
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        super().__init__()

    def __read_box(self, input_data: bytes, return_value: list):
        box_length = read_int_from_data(input_data, 0, 4, "big")
        box_data = input_data[0: box_length]
        box_name = read_string_from_data(box_data, 4, 8, "utf-8")
        box_element = Box(length=box_length, name=box_name, data=box_data[8:])
        return_value.append(box_element)
        if box_name == "moof" or box_name == "traf":
            self.__read_box(box_data[8:], box_element.children)
        if box_length < len(input_data):
            self.__read_box(input_data[box_length:], return_value)

    def print_boxes(self, boxes_list: list, prefix: str = ""):
        """
        Print the structure of the given list. Using recursion add tabulation for every deep level.
        """
        for b in boxes_list:
            print(f"{prefix}Box ID: {b.name} of size {b.length}")
            if len(b.children) > 0:
                self.print_boxes(b.children, prefix + "\t")
            if b.name == "mdat":
                print("Mdat content:")
                print(b.data.decode("utf-8"))

    def parse(self, file_name: str):
        """
        Parse the file with a recursive function and the metadata of the boxes are parsed into a list of elements of
        type `Box` class.
        """
        ret = []
        with open(file_name, "rb") as f:
            data = f.read()
            self.__read_box(data, ret)
        return ret

    def save_image_from_box_mdat(self, box_element: Box, folder: str):
        """
         Save the content of the box in the folder.<br>
         Check Bonus 2 for more information.
        """
        data = read_string_from_data(box_element.data, 0, len(box_element.data), "utf-8")
        bs_data = BeautifulSoup(data, "xml")
        images = bs_data.findAll("smpte:image")
        for img in images:
            file_content = base64.b64decode(img.text)
            with open(f"{folder}{img.get('xml:id')}.{img.get('imagetype')}", "wb") as fh:
                fh.write(file_content)
