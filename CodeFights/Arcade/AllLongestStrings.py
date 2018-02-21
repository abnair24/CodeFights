class AllLongestStrings:
    def __init__(self, inputArray):
        self.inputArray = inputArray

    def all_longest_strings(self):
        max_length = 0
        for i in range(0, len(self.inputArray)):
            max_length = max(max_length, len(self.inputArray[i]))
        return [i for i in self.inputArray if len(i) == max_length]

    @staticmethod
    def get_input():
        print("Enter the array list ")
        return [x for x in input().split()]


if __name__ == '__main__':
    array = AllLongestStrings.get_input()
    all_longest_strings = AllLongestStrings(array)
    print(all_longest_strings.all_longest_strings())









