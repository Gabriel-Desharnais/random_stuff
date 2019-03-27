#! /usr/bin/python3

def greaterThan(*st):
    # This takes any number of string sort them by numeric order and
    # display the result

    # before sorting apply eval on each element and sort them from
    # greatest to smallest
    st = list(st)
    st.sort(key= eval, reverse=True)

    # print the result on screen
    print(*['"%s"'%s for s in st], sep=" is greater than ")

    # return the ordered list
    return st

if __name__ == "__main__":
    result = []
    # test greaterThan function
    test = {}
    # equal stuff
    # I expect equal stuff to be returned in the same order
    test[0] = ["2.3","2.3000"]
    test[1] = ["2.40000","2.4"]
    result.append(test[0] == greaterThan(*test[0]))
    result.append(test[1] == greaterThan(*test[1]))

    # greaterThan stuff
    # int vs int
    test[2] = ["4", "5"]
    test[3] = ["5000", "12"]
    result.append(["5", "4"] == greaterThan(*test[2]))
    result.append(["5000", "12"] == greaterThan(*test[3]))
    # float vs int
    test[4] = ["5", "5.001"]
    test[5] = ["4556", "123.123"]
    result.append(["5.001", "5"] == greaterThan(*test[4]))
    result.append(["4556", "123.123"] == greaterThan(*test[5]))
    # float vs float
    test[6] = ["5.001", "5.002"]
    test[7] = ["4568.01", "457.02"]
    result.append(["5.002", "5.001"] == greaterThan(*test[6]))
    result.append(["4568.01", "457.02"] == greaterThan(*test[7]))
    # exotic
    # leading zeros
    test[8] = ["0.1","00.01"] # if a simple string comparing is done "00.01" is greater
    result.append(["0.1","00.01"] == greaterThan(*test[8]))
    # ending by zeros
    test[9] = ["0.5","0.6000"]
    result.append( ["0.6000", "0.5"] == greaterThan(*test[9]))
    # negatif numbers
    test[10] = ["-6","-5"]
    result.append(["-5", "-6"] == greaterThan(*test[10]))

    if False not in result:
        print("All test have been passed")
    else:
        print("error", result)
