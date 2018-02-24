# For n = 240, the output should be
# lateRide(n) = 4.
#
# Since 240 minutes have passed, the current time is 04:00. The digits sum up to 0 + 4 + 0 + 0 = 4, which is the answer.
#
# For n = 808, the output should be
# lateRide(n) = 14.
#
# 808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.


def lateRide(n):
    hr = int(n / 60)
    minut = n % 60
    total = int(hr / 10) + hr % 10 + int(minut / 10) + minut % 10
    return total
