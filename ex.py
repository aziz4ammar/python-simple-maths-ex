#French version
while True:
    x=int(input('Donner un entier='))
    y=int(input('Donner un autre entier='))
    op=input('opérateur(+,-,*,/)=')
    if op=='+':
        print('la somme de ',x,' + ', y ,'=',x+y)
    if op=='*':
        print('la multiplication de ',x,' * ', y ,'=',x*y)
    if op=='-':
        print('la soustraction de ',x,' - ', y ,'=',x-y)
    if op=='/':
        if y != 0 :
            print('la division de ',x,' / ', y ,'=',x/y)
        else:
            print('division par zéro !')
    q=input('Taper o pour quitter=')
    if q=='o':
        break
