for _ in range(int(input())):
	n = int(input())
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	
	noA = 0
	noB = 0
	
	for i in range(n):
		if A[i] > B[i]:
			noA += 1
		elif B[i] > A[i]:
			noB += 1

	x = ''
	if noA == noB:
		x  = 'DRAW'
	elif noA>noB:
		x = 'A'
	else:
		x = 'B'
	p = str(noA)+' '+str(noB)+' '+x
	print(p)
			
