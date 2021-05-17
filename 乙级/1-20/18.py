"""
Python超时， C++ AC
"""
n = int(input())
lst = [0, 0, 0]  # 记录甲的胜， 平， 负的次数
gestureX = [0, 0, 0]    # 记录甲 石头，剪刀， 布的获胜次数
gestureY = [0, 0, 0]    # 记录乙 石头，剪刀， 布的获胜次数
for i in range(n):
    x, y = input().split()
    if x == 'C':
        if y == 'C':
            lst[1] += 1
        elif y == 'J':
            lst[0] += 1
            gestureX[0] += 1
        else:
            lst[2] += 1
            gestureY[2] += 1
    elif x == 'J':
        if y == 'J':
            lst[1] += 1
        elif y == 'B':
            lst[0] += 1
            gestureX[1] += 1
        else:
            lst[2] += 1
            gestureY[0] += 1
    else:
        if y == 'B':
            lst[1] += 1
        elif y == 'C':
            lst[0] += 1
            gestureX[2] += 1
        else:
            lst[2] += 1
            gestureY[1] += 1
print(*lst)
print(*lst[::-1])
# C, J, B
maxX = 'B' if gestureX[2] >= gestureX[0] and gestureX[2] >= gestureX[1] else ('C' if gestureX[0] >= gestureX[1] else 'J')
maxY = 'B' if gestureY[2] >= gestureY[0] and gestureY[2] >= gestureY[1] else ('C' if gestureY[0] >= gestureY[1] else 'J')
print(maxX, maxY)

# #include <iostream>
# using namespace std;
#
# // 胜， 平， 负
# // C, J, B
# int a[3], gx[3], gy[3];
#
# int main()
# {
# 	int n;
# 	scanf("%d", &n);
# 	for (int i = 0; i < n; ++i)
# 	{
# 		char x, y;
# 		cin >> x >> y;
# 		if (x == y)
# 		{
# 			a[1]++;
# 			continue;
# 		}
# 		if (x == 'C')
# 		{
# 			if (y == 'J')
# 			{
# 				a[0]++;
# 				gx[0]++;
# 			}
# 			else
# 			{
# 				a[2]++;
# 				gy[2]++;
# 			}
# 		}
# 		else if (x == 'J')
# 		{
# 			if (y == 'B')
# 			{
# 				a[0]++;
# 				gx[1]++;
# 			}
# 			else
# 			{
# 				a[2]++;
# 				gy[0]++;
# 			}
# 		}
# 		else
# 		{
# 			if (y == 'C')
# 			{
# 				a[0]++;
# 				gx[2]++;
# 			}
# 			else
# 			{
# 				a[2]++;
# 				gy[1]++;
# 			}
# 		}
# 	}
# 	printf("%d %d %d\n", a[0], a[1], a[2]);
# 	printf("%d %d %d\n", a[2], a[1], a[0]);
# 	char mx = (gx[2] >= gx[1] && gx[2] >= gx[0]) ? 'B' : (gx[0] >= gx[1] ? 'C' : 'J');
# 	char my = (gy[2] >= gy[1] && gy[2] >= gy[0]) ? 'B' : (gy[0] >= gy[1] ? 'C' : 'J');
# 	printf("%c %c", mx, my);
# 	return 0;
# }