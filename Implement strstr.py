def strstr(str, substr):
    if substr not in str:
        return -1
    else:
        for char in range(len(str)-len(substr) + 1):
            if str[char:char+len(substr)] == substr:
                return char

# your Code goes here
if __name__=='__main__':
    n = int(input())
    for i in range(n):
        str,substr = input().strip().split()
        print(strstr(str, substr))
# Contributed by :Harshit Sidhwa

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

# Your task is to complete this function
# you may python module's
