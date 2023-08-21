from pathlib import Path
from unittest import TestCase

from playwright_nodejs import Nodejs


class TestNodejs(TestCase):
    def test_nodejs(self):
        source = Path('test.js')
        js = "console.log(result)"
        re = Nodejs(source=source).call(js).exec()
        print(re)
        self.assertIn('Hello World!', re)
