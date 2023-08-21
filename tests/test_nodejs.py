from pathlib import Path

from playwright_nodejs import Nodejs

js = "console.log(result)"

re = Nodejs(source=Path('test.js')).call(js).exec()
print(re)
