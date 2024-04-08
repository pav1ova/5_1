import unittest
import random

list = []

n=5
for i in range(n):
    list.append(random.randint(0, 99))
print("Случайный список:", list)

def sorting(nums):

    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        sorting(left)
        sorting(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1

    return nums


print ("Упорядоченный список:", sorting(list))


class TestSort(unittest.TestCase):

    def test1(self):
        b = [325, 84, 751, 11, 45, 784]
        c = sorted(b)
        print ("Test №1:",c)
        self.assertEqual(sorting(b), c)

    def test2(self):
        b =  [35, -12, 47, -22, 88, 451, 4, -32, 8]
        c = sorted(b)
        print ("Test №2:",c)
        self.assertEqual(sorting(b), c)

    def test3(self):
        b = [781, 60, 14, 86, 39, 139, 64]
        c = sorted(b)
        print ("Test №3:",c)
        self.assertEqual(sorting(b), c)



suite = unittest.TestLoader().loadTestsFromTestCase(TestSort)
unittest.TextTestRunner(verbosity=2).run(suite)