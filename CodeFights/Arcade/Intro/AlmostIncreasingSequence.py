class AlmostIncreasingSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    @staticmethod
    def get_input():
        print("Enter the array list ")
        return [int(x) for x in input().split()]

    def almost_increasing_sequence(self):
        count = 0
        i = 0
        while i < len(self.sequence) - 2:
            current = self.sequence[i]
            first = self.sequence[i + 1]
            second = self.sequence[i + 2]

            if current < first and first >= second:
                if current >= second:
                    self.sequence.pop(i + 2)
                else:
                    self.sequence.pop(i + 1)
                count += 1;
            elif current >= first and first < second:
                if current >= second:
                    self.sequence.pop(i)
                    i = i + 1;
                else:
                    self.sequence.pop(i + 1)
                count += 1;
            elif current >= first or first >= second and current > second:
                return False
            else:
                i = i + 1;

        if count > 1:
            return False
        return True


if __name__ == '__main__':
    stat = AlmostIncreasingSequence.get_input()
    seq= AlmostIncreasingSequence(stat)
    print(seq.almost_increasing_sequence())

