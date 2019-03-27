# Question
---

The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

---

# Theory

This is simple to do with the `eval` function wich parses a string and interpret it as a python expression.

# how it works
This simple module can be imported with
```python3
import gt
```
It can be used with

```python
gt.greaterThan(st1, st2)
```
You can pass as many string as you want and the function prints something allong the lines of:
```
"5" is greater than "4"
```
the function also returns a sorted list from greatest to smallest of all the string given

This function do not manages garbage given to it so give only numbers or it will break. The usage of eval to do the work highly reduces the number of line but also reduces the security of the software.
