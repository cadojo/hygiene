# Hygiene
_Simple tools to help with module hygiene!_

## Quick Start

This package is pretty simple! It provides a single function, `cleanup`, which
deletes all `locals` which are not listed in an "export" variable of your choice
(this variable defaults to the name `__export__`). Using this function at the 
end of your Python modules helps you keep only the essential items in the namespace!
See the usage example below. See the [Overview](readme) for more information.

## Usage

```python
"""your_module.py

A super helpful Python file/module!
"""

__export__ = [
    "my_function",
    "another_function",
]

from typing  import T
from hygiene import cleanup

def my_function(x: T):
    ...

def another_function(x: T):
    ...

exec(cleanup())
```

```python
"""Code which ~uses~ your_module"""

from your_module import *
# your namespace now has my_function and another_function, nothing else!
```

## Contents

* [Overview](readme)
* [License](license)
* [Authors](authors)
* [Changelog](changelog)
* [Credits](api/modules)