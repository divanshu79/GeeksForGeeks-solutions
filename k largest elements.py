for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	arr.sort(reverse= True)
	lis = arr[:k]
	ans = ''
	for i in range(k):
		ans += str(lis[i]) + " "
	print(ans)