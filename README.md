# List Assignment — README

**Project:** Simple Python list operations  
**File:** `list assignment.py`

## Overview
This small script demonstrates common list operations in Python: creation, insertion, extension, popping, sorting, and finding an index. It's intended for beginners learning how to work with Python lists and to be used as a reference or teaching example.

## Requirements
- Python 3.6+ (works fine on any modern Python 3.x)
- No external dependencies

## File structure
- `list assignment.py` — the main script that performs the list operations and prints results.

## Usage
1. Clone or download the repository containing `list assignment.py`.
2. Run the script from the command line:

```bash
python "list assignment.py"
```

(If your shell rejects the space in the filename, rename the file to `list_assignment.py`.)

## What the script does (step-by-step)
1. **Create an empty list**
   ```py
   my_list = []
   ```
2. **Append elements** — adds `10, 20, 30, 40`
   ```py
   my_list.append(10)
   my_list.append(20)
   my_list.append(30)
   my_list.append(40)
   ```
3. **Insert an element** — inserts `15` at index `1` (second position)
   ```py
   my_list.insert(1, 15)
   ```
4. **Extend the list** — extends with `[50, 60, 70]`
   ```py
   my_list.extend([50, 60, 70])
   ```
5. **Pop last element** — removes the last item (`pop()`)
   ```py
   my_list.pop()
   ```
6. **Sort the list** — sorts in ascending order
   ```py
   my_list.sort()
   ```
7. **Find index** — finds and prints the index of the element `30`
   ```py
   index_of_30 = my_list.index(30)
   ```

## Example output
Running the script prints intermediate results. Example console output (approx.):


```
List after insertion: [10, 15, 20, 30, 40]
List after extension: [10, 15, 20, 30, 40, 50, 60, 70]
List after popping last element: [10, 15, 20, 30, 40, 50, 60]
List after sorting: [10, 15, 20, 30, 40, 50, 60]
Index of 30: 3
```

## Tips & suggestions
- Rename the file to `list_assignment.py` (no spaces) to avoid shell quoting issues.
- Try different methods: e.g., use `sorted(my_list)` if you want a sorted copy rather than sorting in place.
- Add error handling when using `index()` — it raises `ValueError` if the item is not found:
  ```py
  if 30 in my_list:
      print(my_list.index(30))
  else:
      print("30 not in list")
  ```

## Learning exercises (optional)
- Replace `.append()` calls with a single list literal initialization.
- Practice removing a specific value with `remove()` vs `pop(index)`.
- Insert negative values then sort — observe ordering.

## License
This educational snippet is free to use, adapt, and share.
