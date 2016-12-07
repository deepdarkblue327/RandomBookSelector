# RandomBookSelector
Select a random book from a directory given

# Usage
```python
import RandomBookSelector
rbs = RandomBookSelector("PATH_TO_BOOKS_LOCALLY")
rbs.find_random(file_format="epub",exclude=False)
```
The above code gives a random book as a string that you can read next. 

You want a book that is not in the mobi format? Just give exclude as True and provide the format as mobi.

