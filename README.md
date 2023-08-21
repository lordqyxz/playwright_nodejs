# Description

There is a Node.js environment in playwright, why not just use it?

# example

```python
from pathlib import Path

from playwright_nodejs import Nodejs

source = Path('test.js')
js = "console.log(result)"
re = Nodejs(source=source).call(js).exec()
print(re)
```