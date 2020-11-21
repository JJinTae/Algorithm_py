# string.isalpha()
# 알파벳인지 확인한다. 숫자, 기호 및 공백은 False를 리턴한다.

ex1 = 'Hello'
ex2 = 'h'
ex3 = 'Hello Python'
ex4 = '153Python'
ex5 = '153'

ex1.isalpha() # True
ex2.isalpha() # True
ex3.isalpha() # False
ex4.isalpha() # False
ex5.isalpha() # False



# string.isdigit()
# 숫자인지 확인한다. 알파벳, 기호 및 공백은 False를 리턴한다.

ex1 = '123456'
ex2 = '010-1234-5678'
ex3 = 'A1B4'

ex1.isdigit() # True
ex1.isdigit() # False
ex1.isdigit() # False



# string.isalnum
# 알파벳 또는 숫자인지 확인한다. 기호 및 공백은 False를 리턴한다.

ex1 = 'hi'
ex2 = 'hi 33'
ex3 = 'hi33'
ex4 = '1.test'

ex1.isalnum() # True
ex2.isalnum() # False
ex3.isalnum() # True
ex4.isalnum() # False