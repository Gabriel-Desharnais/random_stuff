 # Question
 ---

 Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

---

# Theory

This problem is a simple mathematical problem. To solve it mathematically we could use set theory. [x1;x2] ∩ [x3;x4], if the result is anything but ∅, then the line intersects. Since I don't want to use math library for this, I,ll do a class `line` with an intersection operator (&) and if it returns `None` then they don't intersct.

# How to use it

You can import it with
``` python
import line
```

Then create your lines
``` python
l1 = line.line(x1, x2)
l2 = line.line(x3, x4)
```
intersect the lines
``` python
i = l1 & l2
```

if `bool(i)` returns True the two lines intersects else they don't

# How to test
If you run the python file as is `python line.py` you can see the results of unittest. The test passed on python 3.7.
