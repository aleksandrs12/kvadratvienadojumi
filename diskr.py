print( "hi" )
print( "risināšu kvadrāvienādojumus" )
print( "ax²+-bx+-c=0" )
while True:
    a = float( input( "впишите а" ) )
    b = float( input( "впишите b" ) )
    c = float( input( "впишите c" ) )
    ddd = b ** 2
    dd = 4 * a * c
    d = ddd - dd
    if d > 0:
        x1 = (d ** 0.5 + b * -1) / (2 * a)
        print(x1)
        x2 = (b * -1 - d ** 0.5) / (2 * a)
        print(x2)
        
    elif d == 0:
        x1 = (d ** 0.5 + b * -1) / (2 * a)
        print(x1)
    else:
        print('nav atrisinājuma')
    input()
