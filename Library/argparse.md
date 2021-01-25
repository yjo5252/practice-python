# argparse 모듈

argparse 모듈 : 

* 파이썬 스크립트를 개발할 때, 호출 당시 인지값을 줘서 동작을 다르게 하고 싶은 경우 파이썬 내장함수인 argparse 모듈을 사용해 원하는 기능을 개발할 수 있다. 

```python
# 인자값을 받을 수 있는 인스턴스 생성 
parse = argparse.ArgumentParser(description=’사용법 테스트입니다.’)

# 입력받을 인자값 등록 
parser.add_argument(‘—target’, required=True, help=’어느 것을 요구하나’)
parser.add_argument(‘---env’, required=False, default=’dev’, help=’실행환경은 뭐냐’)

# 입력받을 인자값을 args에 저장 (type: namespace)
args = parser.parse_args()

# 입력받을 인자값 출력 
print(args.target)
print(args.env) 
```

* 터미널에서 해당 파이을 실행시키면 실행방법이 노출된다. 
* 인자값으로 target, env을 주고 실행시킨다. 
```terminal 
$python3 argparse_test.py -–target=테스트 –-env=local
테스트 
local 
$python3 argeparse_test.py -targe=테스트 
테스트 
dev 
```

* 추가 인자 설명 [링크](https://brownbears.tistory.com/413)
