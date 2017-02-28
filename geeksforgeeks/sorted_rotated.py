# python3

def find(arr, x, a, b):
    c = (a + b)  // 2
    if arr[c] == x:
        return c
    #print('[{:d}={:d}  -- [{:d}]={:d}  --  [{:d}]={:d}'.format(a, arr[a], c, arr[c], b, arr[b]))
    if a >= b:
        return -1 if arr[b] != x else b
    if arr[a] <= arr[b] and arr[c] >= arr[a] and arr[c] <= arr[b]:
        if x > arr[c]:
            return find(arr, x, c + 1, b)
        return find(arr, x, a, c)
    if arr[c] > arr[a]:
        if x <= arr[c]:
            if x > arr[b]:
                return find(arr, x, a, c)
            return find(arr, x, c + 1, b)
        return find(arr, x, c + 1, b)
    elif arr[c] <= arr[b]:
        if x > arr[c]:
            if x <= arr[b]:
                return find(arr, x, c + 1, b)
            return find(arr, x, a, c)
        return find(arr, x, a, c)
    return -1

if __name__ == '__main__':
    T = int(input())
    resp = []
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        K = int(input())
        resp.append(find(arr, K, 0, len(arr) - 1))
    for _ in range(T):
        print(resp.pop(0))
