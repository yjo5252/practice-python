# list 자료구조 

* list 자료구조는 "순서를 지킨다" -- 자료구조의 역할론
* list은 동적으로 할당이 되어있고 + 동적으로 추가/삭제하고 
* 맨 뒤에 추가 시 상수 시간이지만, 그 외에는 O(n) 이다. 


### list([]) append()
```python
>>>list = [x, y, z, ...]
>>>list.append(r) 
>>>list
[x, y, z, ..., r]
```

### list 추가 함수 append(...)
```python
codes = [] # empty list
for i in range(1, 101, 2):
    codes.append(i)
print(codes)
```

### list network -- more advanced and recommended version
```python
codes = [i for i in range(1, 101, 2)]
```
### list([]) insert(index, data-structre)
* downfall : O(n) 시간 복잡도
```python
>>>list = [ ..., x, y, z, ...]
>>>list.insert(index, r)
>>>list 
[ ..., x, r, y, z, ...] 
```


### 맨 앞에 추가하는 경우 
* downfall: O(kxn) --> 차라리 다른 자료구조 또는 insert() 메소드를 사용해라.
```python
list = [ x, y, z, ... ]
list = [ r ] + list 
list => [r, x, y, z, ...]
```
### list 삭제 함수 del(...)
```python
>>>list = [ ..., x, y, z, ...] # index 위치의 항목이 y 인 경우 
>>>del(list[index])
>>>list 
[ ..., x, z, ... ]
```
### remove로 지우는 경우와 다름
```python
>>>list = [ ..., y, ..., x, y, z, ...] # index 위치의 항목이 두번째 y인 경우 
>>>list.remove(list[index])
>>>list 
[..., x, y, z, ...]
```

### 리스트 내포 
* for 반복문을 통해서 리스트를 추가하는 방법을 간단하게 처리한다. 
```python
list = []
for k in range(1,11):
    list.append( k )
list     # [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list = [ k for k in range(1, 11)]
list     # [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
### 중첩된 for 반복문에 대한 리스트 내포 
```python
[ <수식문> for <반복자1> in <반복객체1> if <반복조건1>
         for <반복자1> in <반복객체1> if <반복조건1> 
         ...
         for <반복자1> in <반복객체1> if <반복조건1>
]
```
----------
* 2021.7.12 (monday) 
* 알고리즘 코딩테스트 교육 day 1
