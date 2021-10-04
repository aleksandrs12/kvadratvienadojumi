print( "hi" )
print( "risināšu kvadrāvienādojumus" )
print( "ax²+-bx+-c=0" )
while True:
    a = float( input( "ievadiet a" ) )
    if a == 0:
        print('nav kvadrātvienādojums')
        continue
    b = float( input( "ievadiet b" ) )
    c = float( input( "ievadiet c" ) )
    d = b ** 2 - 4 * a * c
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
    if input('ja jūs gribas turpināt nospiediet enter, citādi ievadiet kaut ko un tad nospiediet enter'):
        break
