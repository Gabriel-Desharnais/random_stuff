#! /usr/bin/python3
class line:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    def __and__(self,line1):
        #first sort the to lines
        line1, line2 = sorted([self, line1])
        if max(line1.points()) < min(line2.points()):
            return None
        else:
            return "intersects somewhere"
    def __lt__(self, line1):
        # This function will return true if the line1 contain the
        # smallest point
        return ((self.x1 < line1.x1) and (self.x1 < line1.x2)) or \
                ((self.x2 < line1.x1) and (self.x2 < line1.x2 ))
    def points(self):
        return (self.x1, self.x2)


if __name__ == "__main__":
    l1 = line(1,4)
    l2 = line(2,5)
    l3 = line(0,8)
    l4 = line(1,3)
    l5 = line(4,6)

    # test lt opperation
    passed = []

    passed += [(l1 < l2)]
    passed += [(l3 < l2)]
    passed += [not (l1 < l4)]

    if False not in passed:
        print("lesser then test passed")
    else:
        print("lt opperation not working on:",passed)

    # test sorted opperation
    lineList = [l1, l2, l3, l4, l5]
    preSortedLine = [l3, l1, l4, l2, l5]
    sortedLine = sorted(lineList)

    result = [a is b for a, b in zip(preSortedLine, sortedLine)]
    if False not in result:
        print("sorted opperation working")
    else:
        print("not working on", result, preSortedLine, sortedLine)

    # test intersection opperation
    tests = [(l1 & l2, True ),
             (l1 & l3, True ),
             (l1 & l5, True ), # because I include in the line the extremeties
             (l4 & l5, False),
             (l5 & l4, False),
             (l3 & l4, True )]

    results = [bool(a) == b for a, b in tests]
    if False not in results:
        print("intersects opperation working")
    else:
        print("problem on", results, tests)
