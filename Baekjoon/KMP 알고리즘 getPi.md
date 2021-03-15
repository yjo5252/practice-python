## KMP 알고리즘 getPi

### KMP (Knuth, Morris, Pratt)

* 특정 문자열에서 부분문자열을 찾을 때 선형 시간복잡도를 가진다.
* KMP
  * 문자열 패턴 불일치가 발생한 전체 문자열에서 어떤 부분 문자열이 일치했는지 알고 있다
  * 불일치가 발생한 앞 부분에 대해 다시 비교하지 않고 매칭을 수행한다.
  * 매칭에 성공하나 부분문자열에 주목한다.
 * KMP 알고리즘 
  * Processing of the pattern (패턴 전처리 과정) : Degenerate pattern (작은 패턴이 한 번 이상 반복되는 현상)을 찾는다.
  * Pi 배열
  * LPS 배열 : Prefix와 Suffix가 같은 경우 중 가장 길이가 긴 경우 지칭한다.

### pi[] 배열

* 문자열의 각 부분 문자열에서 접미사와 접두사가 **같은 부분의 (prefix ==suffix) 개수를** 저장하고 있다. 
* 예시
```
ABSAB
Prefix: A, AB, ABX, ABSA
Suffix: B, AB, XAB, BXAB

Prefix == Suffix : AB
```
pat = pattern
lps[] 값 : 다음에 조사할 인덱스를 정하는 기준이 된다.

 ### LPS 배열 구하는 코드 
 ```python
 def computeLPS(pat, lps):
   leng = 0 # length of previous longest prefix suffix
   
   # 항상 lps[0] == 0 이므로 while 문은 i=1 부터 시작한다. 
   i = 1
   while i < leng(pat):
     # 이전 인덱스에서 같았다면 다음 인덱스만 비교하면 된다.
     if pat[i] == pat[leng]: 
       leng += 1
       lps[i] = leng 
       i += 1
     else: 
       # 일치하지 않는 경우 
       if leng != 0:
         # 이전 인덱스에서는 같았으므로 leng을 줄여서 다시 검사 
         leng = lps[leng-1]
         다시 검사해야하므로 i는 증가하지 않음
       else:
          # 이전 인덱스에서도 같지 않았다면 lpas[i]는 0이고 i는 1 증가
          lps[i] = 0
          i  += 1
 ```

### KMP Search 




참고 링크: https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/
