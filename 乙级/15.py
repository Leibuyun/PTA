# Python超时， C++ AC
import functools


class P:
    def __init__(self, *args):
        self.id = int(args[0])
        self.d = int(args[1])
        self.c = int(args[2])

firstLst = []
secondLst = []
thirdLst = []
fourthLst = []

lst = input().split()
n, l, h = int(lst[0]), int(lst[1]), int(lst[2])
cnt = 0
for i in range(n):
    p = P(*input().split())
    if p.d < l or p.c < l:
        continue
    cnt += 1
    if p.d >= h and p.c >= h:
        firstLst.append(p)
    elif p.d >= h > p.c:
        secondLst.append(p)
    elif h > p.d >= p.c and p.c < h:
        thirdLst.append(p)
    else:
        fourthLst.append(p)


def cmp1(p1: P, p2: P):
    s1, s2 = p1.d + p1.c, p2.d + p2.c
    if s1 != s2:
        return s2 - s1
    else:
        if p1.d != p2.d:
            return p2.d - p1.d
        else:
            return p1.id - p2.id


firstLst.sort(key=functools.cmp_to_key(cmp1))
secondLst.sort(key=functools.cmp_to_key(cmp1))
thirdLst.sort(key=functools.cmp_to_key(cmp1))
fourthLst.sort(key=functools.cmp_to_key(cmp1))

print(cnt)
for item in firstLst:
    print(item.id, item.d, item.c)
for item in secondLst:
    print(item.id, item.d, item.c)
for item in thirdLst:
    print(item.id, item.d, item.c)
for item in fourthLst:
    print(item.id, item.d, item.c)

# #include <iostream>
# #include <algorithm>
# #include <vector>
# using namespace std;
#
# struct node{
# 	int id, d, c;
# 	node(int id, int d, int c){
# 		this->id = id;
# 		this->d = d;
# 		this->c = c;
# 	}
# };
#
# vector<node> firstLst;
# vector<node> secondLst;
# vector<node> thirdLst;
# vector<node> fourthLst;
#
#
# bool cmp(const node& p1, const node& p2)
# {
# 	int sum1 = p1.d + p1.c;
# 	int sum2 = p2.d + p2.c;
# 	if (sum1 != sum2)
# 		return sum1 - sum2 > 0 ? true : false;
# 	else {
# 		if (p1.d != p2.d)
# 			return p1.d - p2.d > 0? true: false;
# 		else
# 			return p2.id - p1.id > 0? true: false;
# 	}
# }
#
# int main()
# {
# 	int n, l, h;
# 	scanf("%d%d%d", &n, &l, &h);
# 	int cnt = 0;
# 	for (int i = 0; i < n; ++i)
# 	{
# 		int tid, td, tc;
# 		scanf("%d%d%d", &tid, &td, &tc);
# 		if (td < l || tc < l)
# 			continue;
# 		cnt++;
# 		node p = node(tid, td, tc);
# 		if (td >= h && tc >= h)
# 			firstLst.push_back(p);
# 		else if (td >= h && tc < h)
# 			secondLst.push_back(p);
# 		else if (td < h && tc < h && td >= tc)
# 			thirdLst.push_back(p);
# 		else fourthLst.push_back(p);
# 	}
# 	sort(firstLst.begin(), firstLst.end(), cmp);
# 	sort(secondLst.begin(), secondLst.end(), cmp);
# 	sort(thirdLst.begin(), thirdLst.end(), cmp);
# 	sort(fourthLst.begin(), fourthLst.end(), cmp);
# 	printf("%d\n", cnt);
# 	for (int i = 0; i < firstLst.size(); ++i)
# 		printf("%d %d %d\n", firstLst[i].id, firstLst[i].d, firstLst[i].c);
# 	for (int i = 0; i < secondLst.size(); ++i)
# 		printf("%d %d %d\n", secondLst[i].id, secondLst[i].d, secondLst[i].c);
# 	for (int i = 0; i < thirdLst.size(); ++i)
# 		printf("%d %d %d\n", thirdLst[i].id, thirdLst[i].d, thirdLst[i].c);
# 	for (int i = 0; i < fourthLst.size(); ++i)
# 		printf("%d %d %d\n", fourthLst[i].id, fourthLst[i].d, fourthLst[i].c);
# }