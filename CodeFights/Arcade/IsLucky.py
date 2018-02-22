# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.
#
# Given a ticket number n, determine if it's lucky or not.
#
# Example
#
# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.


def islucky(n):
    str_number = str(n)
    length = len(str_number)
    first_half = str_number[0:int(length / 2)]
    second_half = str_number[int(length / 2):int(length)]
    i = 0
    sum_first = 0
    sum_second = 0
    while i < length/2:
        sum_first = sum_first + int(first_half[i])
        sum_second = sum_second + int(second_half[i])
        i = i + 1
    if sum_first == sum_second:
        return True
    else:
        return False


number = input()
print(islucky(number))
