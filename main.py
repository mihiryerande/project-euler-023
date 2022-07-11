# Problem 23:
#     Non-Abundant Sums
#
# Description:
#     A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
#     For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
#       which means that 28 is a perfect number.
#     A number n is called deficient if the sum of its proper divisors is less than n,
#       and it is called abundant if this sum exceeds n.
#
#     As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
#       the smallest number that can be written as the sum of two abundant numbers is 24.
#     By mathematical analysis, it can be shown that all integers
#       greater than 28123 can be written as the sum of two abundant numbers.
#     However, this upper limit cannot be reduced any further by analysis
#       even though it is known that the greatest number that cannot be expressed as
#       the sum of two abundant numbers is less than this limit.
#
#     Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from math import floor, sqrt

# All integers greater than this are known to be abundant sums
# So candidates for non-abundant sums are up to and including this
ABUNDANT_LIMIT = 28123


def main() -> int:
    """
    Returns the sum of all non-abundant sums,
      where a non-abundant sum is a number which cannot be written
      as the sum of two abundant numbers.
    An abundant number is a number for which the sum of
      its proper divisors less than itself
      is greater than the number itself.

    Returns:
        (int): Sum of all non-abundant sums
    """
    global ABUNDANT_LIMIT
    n = ABUNDANT_LIMIT  # To make code easier to read

    # Maintain mapping (as an array) of
    #   each number to its sum of proper divisors
    # Include 1 as a factor of everything to start, then skip while iterating
    div_sums = [1 for _ in range(n)]
    div_sums[0] = 0

    # Iterate through possible pairs of factors and accumulate at relevant multiples
    mid = floor(sqrt(n))
    for f1 in range(2, mid+1):  # Lower divisor
        for f2 in range(f1, n//f1):  # Upper divisor
            m = f1 * f2
            div_sums[m-1] += f1
            div_sums[m-1] += f2
        # Don't double-count divisor f1 for its square
        div_sums[f1**2-1] -= f1

    # Extract abundant numbers (ordered list)
    abundant_nums = list(map(lambda y: y[0]+1, filter(lambda x: x[1] > (x[0]+1), enumerate(div_sums))))

    # Determine all sums of two abundant numbers
    abundant_sums = set()
    for i in range(len(abundant_nums)):  # Lower of pair
        a = abundant_nums[i]
        for j in range(i, len(abundant_nums)):  # Upper of pair
            b = abundant_nums[j]
            abundant_sums.add(a+b)

    # Check all candidates under ABUNDANT_LIMIT for non-abundance
    non_abundant_sum = 0
    for i in range(1, n+1):
        if i not in abundant_sums:
            non_abundant_sum += i

    return non_abundant_sum


if __name__ == '__main__':
    non_ab_sum = main()
    print('Sum of all non-abundant sums:')
    print('  {}'.format(non_ab_sum))
