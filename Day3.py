arr = [215,513,712,803]
start = 0 
end = max(arr) # 배열에서 가장 큰 수
result = 0

while (end - start >= 0):
    sum = 0
    mid = (start + end)//2 # 중앙값 설정 

    for i in arr:
        sum += i//mid #배열의 합을 중앙값으로 나눴을 때

    if sum > 10:
        start = mid +1

    elif sum <10:
        end = mid -1

    else:
        result = mid
        break

print(result)
