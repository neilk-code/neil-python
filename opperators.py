'''
Arithmatic operators
'''
a=13
b=5
c=a/b
d=a//b
e=a%b
print(a,'/',b,'=',c)
print(f'{a}//{b}={d}')
print(f'{a}%{b}={e}')
print(2**2**3)

'''
Reletional  operators
< > <= >= == !=
diffrence between =  and ==
== equality  check LHS==RHS
=   assignment operator  assign right hand side value to left hand side operand
'''
a=13
b=5
c=13
print(f'{a}<{b}={a<b}')
print(f'{a}>{b}={a>b}')
print(f'{a}<={c}={a<=c}')
print(f'{a}=={b}={a==b}')
print(f'{a}=={c}={a==c}')
print(f'{a}!={c}={a!=c}')
print(f'{a}!={b}={a!=b}')