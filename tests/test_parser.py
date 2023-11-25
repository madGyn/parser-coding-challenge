import os
from unittest import TestCase
from parser import Parser
import contextlib


class TestParser(TestCase):
    def test_parse(self):
        try:
            parser = Parser()
            boxes = parser.parse("../data/text0.mp4")
        except Exception:
            self.fail()
        check_boxes = len(boxes) == 2
        self.assertEqual(boxes[0].name, 'moof')
        self.assertEqual(boxes[0].length, 181)
        self.assertEqual(boxes[1].name, 'mdat')
        self.assertEqual(boxes[1].length, 17908)
        check_boxes = check_boxes and len(boxes[0].children) == 2
        self.assertEqual(boxes[0].children[0].name, 'mfhd')
        self.assertEqual(boxes[0].children[0].length, 16)
        self.assertEqual(boxes[0].children[1].name, 'traf')
        self.assertEqual(boxes[0].children[1].length, 157)
        check_boxes = check_boxes and len(boxes[0].children[1].children) == 4
        self.assertEqual(boxes[0].children[1].children[0].name, 'tfhd')
        self.assertEqual(boxes[0].children[1].children[0].length, 24)
        self.assertEqual(boxes[0].children[1].children[1].name, 'trun')
        self.assertEqual(boxes[0].children[1].children[1].length, 20)
        self.assertEqual(boxes[0].children[1].children[2].name, 'uuid')
        self.assertEqual(boxes[0].children[1].children[2].length, 44)
        self.assertEqual(boxes[0].children[1].children[3].name, 'uuid')
        self.assertEqual(boxes[0].children[1].children[3].length, 61)
        self.assertTrue(check_boxes)

    def test_print_boxes(self):
        parser = Parser()
        boxes = parser.parse("../data/text0.mp4")
        try:
            parser.print_boxes(boxes)
            self.assertTrue(True)
        except Exception:
            self.fail()

    def test_save_image_from_box_mdat(self):

        with contextlib.suppress(FileNotFoundError):
            for i in range(1, 4):
                os.remove(f"../data/images/image00{i}.PNG")

        parser = Parser()
        boxes = parser.parse("../data/text0.mp4")
        parser.save_image_from_box_mdat(boxes[1], "../data/images/")

        for i in range(1, 4):
            self.assertTrue(os.path.isfile(f"../data/images/image00{i}.PNG"))
