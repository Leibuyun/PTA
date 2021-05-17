"""
Python超时， C++ AC
"""
from math import sqrt

m, n = input().split()
m, n = int(m), int(n)


def is_prime(num):
    k = int(sqrt(num)) + 1
    for i in range(2, k):
        if num % i == 0:
            return False
    return True


prime_lst = []
for i in range(2, 104730):
    if is_prime(i):
        prime_lst.append(i)

row_first = True
cnt = 0
for i in range(m-1, n):
    if row_first:
        print(prime_lst[i], end='')
        row_first = False
    else:
        print('', prime_lst[i], end='')
    cnt += 1
    if cnt % 10 == 0:
        print()
        row_first = True


# #include <iostream>
# #include <cstdio>
# #include <cmath>
# using namespace std;
#
# int a[10000] = { 2, 3, 5, 7, 11 };
#
# bool isPrime(int num)
# {
# 	for (int i = 2, k = int(sqrt(num)) + 1; i <= k; ++i)
# 		if (num % i == 0)
# 			return false;
# 	return true;
# }
#
# int main()
# {
# 	int cnt = 5;
# 	for (int i = 13; i < 104730; ++i)
# 		if (isPrime(i))
# 			a[cnt++] = i;
# 	bool rowFirst = true;
# 	int m, n;
# 	scanf("%d%d", &m, &n);
# 	cnt = 0;
# 	for (int i = m - 1; i < n; ++i)
# 	{
# 		if (rowFirst)
# 		{
# 			printf("%d", a[i]);
# 			rowFirst = false;
# 		}
# 		else
# 		{
# 			printf(" %d", a[i]);
# 		}
# 		cnt += 1;
# 		if (cnt % 10 == 0)
# 		{
# 			printf("\n");
# 			rowFirst = true;
# 		}
#
# 	}
#
# 	return 0;
# }