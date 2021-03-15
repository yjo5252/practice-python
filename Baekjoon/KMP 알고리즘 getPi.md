## KMP 알고리즘 getPi

### KMP (Knuth, Morris, Pratt)

* 특정 문자열에서 부분문자열을 찾을 때 선형 시간복잡도를 가진다.
* KMKP
  * 문자열 패턴 불일치가 발생한 전체 문자열에서 어떤 부분 문자열이 일치했는지 알고 있다
  * 불일치가 발생한 앞 부분에 대해 다시 비교하지 않고 매칭을 수행한다.
  * 매칭에 성공하나 부분문자열에 주목한다.

### pi[] 배열

* 문자열의 각 부분 문자열에서 접미사와 접두사가 **같은 부분의 (prefix ==suffix) 개수를** 저장하고 있다. 
* 예시
```
ABSAB
Prefix: A, AB, ABX, ABSA
Suffix: B, AB, XAB, BXAB

Prefix == Suffix : AB
```

 
