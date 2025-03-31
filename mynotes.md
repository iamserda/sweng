# Bits2Bytes: My Software Engineering Notes

### A reference to capture assertio errors and lines where they occurred.

````python
"""How to show the line for assertions raised during a function call."""
import sys
import traceback

def my_function():
    try:
        assert True
        assert 7 == 7
        assert 1 == 2  # This will fail
    except AssertionError:
        _, _, tb = sys.exc_info()
        traceback.print_tb(tb)  # Fixed format
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]

        print(f'An error occurred on line {line} in statement {text}')
        exit(1)```
````

### [How to count relevant lines of code in your Git Repo](https://gist.github.com/mandiwise/dc53cb9da00856d7cdbb)

```bash
find . -type d \( -name "node_modules" -o -name "env" \) -prune -o -type f \( -name "*.py" -o -name "*.js" \) -print0 | xargs -0 wc -l
```
