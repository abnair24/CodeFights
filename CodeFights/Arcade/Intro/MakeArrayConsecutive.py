#
# For statues = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(statues) = 3.
#
# Ratiorg needs statues of sizes 4, 5 and 7.


class MakeArrayConsecutive:
    def __init__(self, statues):
        self.statues = statues

    def consecutive(self):
        max_value = max(self.statues)
        min_value = min(self.statues)
        if (max_value - min_value) == (len(self.statues) - 1):
            return 0
        else:
            return (max_value - min_value) - (len(self.statues) - 1)

    @staticmethod
    def get_input():
        print("Enter the array list ")
        return [int(x) for x in input().split()]


if __name__ == '__main__':
    stat = MakeArrayConsecutive.getInput()
    makeArrayConsecutive = MakeArrayConsecutive(stat)
    print("makeArrayConsecutive...  ")
    print(makeArrayConsecutive.consecutive())




