num = [1,2,3,4,5,6,7,8,9,10]
def lagest_product(n):
    cur = 0
    max_product = float('-inf')
    left = 0
    right = n-1
    while right<len(num):
        cur = 1
        for i in range(left,right+1):
            cur*=num[i]
        max_product = max(max_product,cur)
        right+=1
        left+=1
    return max_product
print(lagest_product(3))
