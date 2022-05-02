# standard modules
import unittest

# external modules

# project modules
from src.db import queryconverter

class TestToObjArray(unittest.TestCase):

    def test_fullconvert(self):
        expected = [
            {"id":1,"firstName":"Logan","lastName":"Lucky","email":"ll@llmail.com"},
            {"id":2,"firstName":"George","lastName":"Gorgeous","email":"gg@ggmail.com"},
            {"id":3,"firstName":"John","lastName":"Johnson","email":"mrjj@johnson.com"}
        ]
        result = queryconverter.to_obj_array(
            [
                [1,"Logan","Lucky","ll@llmail.com"],
                [2,"George","Gorgeous","gg@ggmail.com"],
                [3,"John","Johnson","mrjj@johnson.com"]
            ],
            ["id", "firstName", "lastName", "email"]
        )
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()