# Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
#
# Example
#
# For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
# sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

class SortByHeight:
    def __init__(self, sequence):
        self.sequence = sequence

    @staticmethod
    def get_input():
        print("Enter the array list ")
        return [int(x) for x in input().split()]

    def sort_by_height(self):
        p = iter(sorted(item for item in self.sequence if item > 0))
        return [t if t < 0 else next(p) for t in self.sequence]


if __name__ == '__main__':
    s = SortByHeight.get_input()
    sortByHeight = SortByHeight(s)
    print(sortByHeight.sort_by_height())
