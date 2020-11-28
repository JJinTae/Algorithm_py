양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.<br>
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.<br>

#

~~~python
def solution(x):
    
    L = list(map(int, list(str(x))))
    
    return x % sum(L) == 0
~~~

+ map
~~~python
    L = list(map(int, list(str(x))))
~~~
> map에 int와 리스트를 넣으면 list(str(x))의 모든 요소를 int를 사용해서 변환한다. <br>
그 다음 list를 사용해서 map의 결과를 다시 리스트로 만들어준다.

이처럼 각 자릿수의 정수를 L에 담을 수 있다.

~~~python
return x % sum(L) == 0
~~~

L 리스트의 모든 합을 구하는 sum()을 사용한 후 x의 나머지를 판별하여 하샤드 수를 확인한다.
