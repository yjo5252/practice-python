## N개의 공정시간 
15회 (2019년 9번) (2018년 10번) 기출

### * 문제 
```
[문제]

N개의 작업 공정이 있습니다. 공정마다 소요되는 시간이 있고, 각 공정들 끼리 선후 관계가 존재할 때는 반드시 선행 공정이 끝나야만 다음 공정으로 넘어갈 수 있습니다.

예를 들어 아래 공정을 보면, A공정에 10이 소요되고 난 후, B와 C가 동시에 진행이 됩니다. 이 때 B공정이 끝나는 시점은 30이 되고, C공정은 110에 끝나게 됩니다. 이 때 D공정은, B와 C가 모두 끝나는 시점인 (즉,C가 끝나는 시점) 110에 시작하게 되고, 따라서 D공정은 130에 끝나게 됩니다.

이러한 원칙을 적용하여, 임의로 주어지는 공정에 대해 목표되는 공정까지 소요되는 최소시간을 구하는 프로그램을 작성하세요.

[제한사항]

-      공정수 N과 N사이의 관계수는 모두 1이상 100이하의 정수입니다.

-      N개의 각 공정에서 소요되는 시간을 저장하기 위해 사용되는 배열 N은 1차정수배열입니다.

-      N개의 공정간의 관계가 저장된 Relation은 2차정수배열입니다. -- 이해를 돕기위해 그림에서는 공정번호를 A,B,C,D로 사용하여 설명하였으나 N개의 공정번호 역시 정수를 사용합니다. -- 공정간의 관계는 [앞공정번호 뒷공정번호] 순이며, 그림에서 A->B , B->C, A->C의 관계가 성립할 때 [[1,2], [2,3], [1,3]] 로 주어지며, 이때 Relation의 행크기는 3, 열크기는 2입니다.

-      N의 크기(공정수)와 Relation의 행크기(공정간의 관계수)는 모두 1이상 100이하의 정수임을 다시 한번 강조합니다.


[입력 형식]

- 첫 째줄에 공정수(N)와 관계수(R)를 입력한다. (1 ≤ N,R ≤ 100)

- 그 다음 줄에 각 공정에서 소요되는 시간 N개를 입력하 고, 그 다음 줄 부터 공정간의 관계가 R줄에 걸쳐 입력한 다. 공정간의 관계는 연결되는 공정 번호가 "앞공정번호 뒷공정번호" 순으로 나온다.

- 그 다음 줄에 목표되는 공정 번호를 입력한다.


[출력 형식]

- 최소 소요시간을 출력한다.
```

* 입력예시 
```
4 4
10 20 100 20
1 2
1 3
2 4
3 4
4
```

* 출력 결과 : 130

### * 풀이법 
- 풀이 아이디어 
  * 각 공정의 시간을 저장 = 배열 
  * 첫번째 공정을 시작으로 공정 탐색 = 큐 
  
- 필요 코드 
  * 선입선출 큐를 사용한다. (위상정렬, indegree=0부터 큐에 입력한다)
  * 시간을 저장할 배열. total 을 초기화한다.
  * for/while 반복문을 사용한다.
  
- 문제 조건 
  * 매 공정 진행시 배열을 사용해 해당 공정에 걸린 시간을 저장한다. 

### * python 문법 
1. 2차원 배열 0으로  초기화 
```python
adj=[[0]*len(n) for _ in range(len(n))]
```
2. 입력값을 초기화
* 변수 2개
```python 
N, R = (map(int, input().split()))
```
* 리스트
```python
n = list(map(int, input().split()))
```
* 2차원 배열 
```python
r = [list(map(int, input().split())) for _ in range(R)]
```


### * 코드 
```python
import copy 
from queue import Queue

def solution (n, r, goal):
    # python input 여러 줄로 받은 거 잘 나눴다 치고... 

    time=copy.deepcopy(n)
    adj = [[0]*len(n) for _ in range(len(n))]
    indegree=[0]*len(n)
    total=[0]*len(n)
    que = Queue()

    for row in r:
        X1 = row[0]-1
        X2 = row[1]-1
        adj[X1][X2] = 1
        indegree[X2] +=1

    for i in range(len(n)):
        if(indegree[i] == 0):
            total[i]=time[i]
            que.put(i)

    while (not que.empty()):
        q = que.get()
        for i in range(len(n)):
           if (adj[q][i]==1): 
               total[i] = max(total[i], total[q] + time[i])
               indegree[i]-=1
               if (indegree[i]==0):
                    que.put(i)
    
    return total[goal-1]

N, R = map(int, input().split()) # 공정 개수 # 관계수
n = list(map(int, input().split()))
r = [list(map(int, input().split())) for _ in range(R)]
goal = int(input())
print(solution(n, r, goal))
```
