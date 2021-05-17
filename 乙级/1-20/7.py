"""
Python超时， C++ AC
"""
import math

n = int(input())
prime = [2, 3]


def is_prime(n):
    k = int(math.sqrt(n))
    for i in prime:
        if i > k:
            break
        if n % i == 0:
            return False
    return True


cnt = 0
for j in range(5, n + 1):
    if is_prime(j):
        prime.append(j)
        if prime[-1] - prime[-2] == 2:
            cnt += 1
print(cnt)

# include <iostream>
# #include <cmath>
# bool a[100000];
# int is_prime(int num){
#     for(int i = 2, k = int(sqrt(num)) + 1; i < k; ++i)
#         if(num % i == 0)
#             return false;
#     return true;
# }
# int main(){
#     int n;
#     scanf("%d", &n);
#     for(int i=2;i<=n;++i)
#         if(is_prime(i))
#             a[i] = true;
#     int cnt = 0;
#     for(int i=3;i<=n-2;i+=2)
#         if(a[i] && a[i+2])
#             cnt++;
#     printf("%d\n", cnt);
#     return 0;
# }
