# Exercise 4: Gridlock in Bristol

Road works are taking place across Bristol. Now that the project is finished, the construction company needs to pick up all the traffic cones.
However, due to the physical size of the construction workers, they cannot squeeze into tight spaces. Specifically, workers cannot access a cone if it is too heavily surrounded. A cone can only be removed if it has fewer than four cones in its eight immediately adjacent positions (horizontal, vertical, and diagonal). If a cone has four or more adjacent cones, it is blocked and must be left behind for now.
As cones are successfully removed, spaces clear up, which may allow workers to access previously blocked cones in the next step. This process repeats in discrete steps until no more cones can be removed, and the grid stabilises.
Below is a demonstration of the cleanup process. `^` represents a traffic cone, `.` represents an empty space and `_` represents a freshly removed cone.


## Examples
```python

Initial State
^..^..
..^^^.
...^^.
^^..^.
^^^^..
^^^..^

Cleanup Step 1
_.._..
.._^^.
...^^.
_^.._.
^^^_..
_^^.._

Cleanup Step 2
......
...__.
...__.
._....
_^^...
.^_...

Cleanup Step 3
......
......
......
......
.__...
._....

Final State
......
......
......
......
......
......
```


In this example it is possible for the construction workers to remove all cones and the iteration trivially terminates. Will this always be the case?

Using your puzzle input, iteratively simulate cone cleanup. Calculate how many cleanup steps occur before no more cones can be removed.
