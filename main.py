def karatsuba(x, y): #N1
    # Caso base para números pequenos
    if x < 10 or y < 10:    #N2
        return x * y #N3

    # Calcula o tamanho dos números
    n = max(len(str(x)), len(str(y)))   #N4
    m = n // 2  #N5

    # Divide os números em duas partes
    high_x, low_x = divmod(x, 10**m)  #N6
    high_y, low_y = divmod(y, 10**m)    #N7

    # 3 chamadas recursivas
    z0 = karatsuba(low_x, low_y)    #N8
    z1 = karatsuba((low_x + high_x), (low_y + high_y)) #N9
    z2 = karatsuba(high_x, high_y)  #N10

    # Combina os resultados
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0     #N11