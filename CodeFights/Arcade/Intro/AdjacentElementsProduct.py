# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
# Guaranteed constraints:
# 2 ≤ inputArray.length ≤ 10,
# -1000 ≤ inputArray[i] ≤ 1000.


class AdjacentElementsProduct:
    def __init__(self, input_array):
        self.input_array = input_array

    def adjacent_elements_product(self):
        original = -1001000
        length = len(self.input_array)
        for i in range(0, length - 1):
            prod = self.input_array[i] * self.input_array[i + 1]
            if prod >= original:
                original = prod
        return original

    @staticmethod
    def get_input():
        print("Enter the array list ")
        return [int(x) for x in input().split()]


if __name__ == '__main__':
    stat = AdjacentElementsProduct.get_input()
    adjust_elements_product = AdjacentElementsProduct(stat)
    print("AdjacentElementsProduct...  ")
    print(adjust_elements_product.adjacent_elements_product())
