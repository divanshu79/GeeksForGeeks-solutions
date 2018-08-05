for _ in range(int(input())):
q = int(input())
arr = []
for i in range(q):
	num = list(map(int, input().split()))
	if num[0] == 3:
		if len(arr) == 0:
			print(-1)
		else:
			print(arr[0])
	elif num[0] == 2:
		arr.pop(0)
	else:
		arr.append(num[1])