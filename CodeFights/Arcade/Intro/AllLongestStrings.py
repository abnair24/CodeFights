class AllLongestStrings:
    def __init__(self, inplist):
        self.inplist = inplist

    def alllongeststrings(self):
        maxlen = len(self.inplist[0])
        i = 0
        newlist = []
        if len(self.inplist) == 1:
            newlist.append(self.inplist[0])
        while i < len(self.inplist) - 1:
            if maxlen == len(self.inplist[i + 1]):
                if i == 0:
                    newlist.append(self.inplist[i])
                newlist.append(self.inplist[i + 1])
            elif maxlen < len(self.inplist[i + 1]):
                newlist.clear()
                newlist.append(self.inplist[i + 1])
                maxlen = len(self.inplist[i + 1])
            else:
                if i == 0:
                    maxlen = len(self.inplist[i])
                    newlist.append(self.inplist[i])
            i += 1

        return newlist

    @staticmethod
    def get_input():
        print("Enter the array list ")
        return [x for x in input().split()]


if __name__ == '__main__':
    array = AllLongestStrings.get_input()
    all_longest_strings = AllLongestStrings(array)
    print(all_longest_strings.alllongeststrings())


