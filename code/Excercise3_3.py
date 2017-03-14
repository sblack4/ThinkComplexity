import unittest

def bisection(sortedList, targetValue):
    """
    implementation of bisect algorithm
    see python's https://docs.python.org/2/library/bisect.html module
    """
    listLength = len(sortedList)
    if listLength == 0:
        return None
    currentIndex = listLength/2
    currentValue = sortedList[currentIndex]
    if targetValue == currentValue:
        return currentIndex
    elif targetValue > currentValue:
        return bisection(sortedList[currentIndex:listLength], targetValue) + currentIndex
    else:
        return bisection(sortedList[0:currentIndex], targetValue)

class Tests(unittest.TestCase):
    def test_bisection1(self):
        list1 = [1,2,3,4,5,6]
        target1 = 4
        index1 = bisection(list1, target1)
        self.assertEqual(index1, 3)

    def test_bisection2(self):
        list2 = [0,1,2,3,4,5,6,7,8,9]
        target2 = 4
        index2 = bisection(list2, target2)
        self.assertEqual(index2, 4)

    def test_bisection3(self):
        list3 = [0,2,4,5,6,9]
        target3 = 4
        index3 = bisection(list3, target3)
        self.assertEqual(index3, 2)

if __name__ == '__main__':
    unittest.main()

    