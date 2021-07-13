
# 이분탐색 
* 정렬된 데이터에서 원하는 값을 찾는 방법 
    * left, right 변수값을 찾고자 하는 검색


* 특징 
    * 비교하는 비용이 O(f(N))일 때, 전체 비용은 O(f(N)logN)
    * 찾고자 하는 값을 정확하게 모를 때에는 Pass - Fail 방법 이용한다. 
    * L | R 이 이웃했다. L 보다 작으면 Fail, R 이상이면 True 
    
```
1 - 10 : 10/2 - 1 = 4 
.. 4 .. 10 : 14 / 2 = 7 
.. 4 .. 7 .. 10 

11/2 = 5 
4 5 => 답은 5이다.

```


## 문제 1. 입국심사 
* 코딩테스트에 웬만하면 다 있다.~ ! 
* 중급 난이도 (75%)
### 문제풀이 
* 이분탐색 pass - fail 방법을 사용한다. 

2n을 기준으로 (P)
(가장 빨리 처리하는 사람) x n 

 * T 시간 안에 pass 를 할 꺼냐 안할꺼냐를 어떻게 알까? 
    * T 시간 안에 심사 위원이 몇시간 걸릴 지 계산. 
```
예) 42분 , 6명이 7 분짜리 심사관에게 대기하여 심사 받는다. 
예) 0분 
0과 42의 중앙값 21분 

21분동안) 7분 * 3명 + 10분 * 2명. 총 5명. 따라서 21 분은 fail.
(사람 수가 6보다 크거나 같은지 봤을 때 작으므로 fail)

21과 42의 중앙값 31분 
31분동안) 7분 * 4명 + 10분 * 3명. 총 6명. 따라서 pass.

21과 31분의 중앙값 26. 
26분동안 fail 

26과 31 분의 중앙값 28. 
28분동안 pass 

26과 28의 중앙값 27
27분동안 fail 

답 28

```

### 코드 

```python
n = int(input()
ofs = list(map(int, input().split()))

left, right = 0, ofs[0]*n   # 무조건 fail 조건, 무조건 pass 조건
while left+1 < right: # 이웃하지 않았다. => 중앙값을 구해서 범위 조절한다. 
    mid = (left+right)//2
    prs = 0
    for o in ofs: 
        prs += mid // o
    if prs >= n: right = mid 
    else: left = mid

```



## 문제 2. 롤케이크 자르기 
* 예외를 허용하지 않고 코드를 짜려면 '가드'를 설정하는 게 좋다. 
    * add [0, L] into cuts list for convinient search 
    * cut 사이의 간격이 중요함.
    * 0 ... (C[i] - C[i-1])  ... L 
    * 0. L을 가이드라인으로 제공 
* 중상급 난이도 문제 (80%)


### 이분탐색을 사용한 문제 풀이 (Pass-Fail)

* 입력예제 
```
10 2 1 
4 5 
```
* 출력: 5 5 
* 코드 
```python
from bisect import bisect_left
L, K, C = map(int, input().split())
cuts = list(map(int, input().split()))

# add [0, L] into cuts list for convinient search 
cuts += [ 0, L ]
cuts.sort()

# pass-fail : pass: boolean, first-cut:int
def isPass(cuts, longest, c):
    cur = cuts[-1] # L
    while c > 0: # 자를 수 있다. 자르는 횟수
        f = cur - longest 
        if f <= 0: return True, cuts[1] # ? 인접해있다+
        idx = bisect_left(cuts, f) # < long <= 
        if cur == cuts[idx]: # 더 이상 자를 수 없다.
            return False, 0
        cur = cuts[idx] 
        c -= 1
    if cur > longest: return False, 0
    return True, cur

# binary search
left, right = 0, L
firstCut = L 
while left+1 < right: 
    mid = (left+right)//2
    r, fc = isPass(cuts, mid, C)
    if r: 
        right = mid
        firstCut = fc
    else: left = mid

print(right, firstCut)



```
