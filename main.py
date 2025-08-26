def karatsuba(x, y):
    # Caso base para números pequenos
    if x < 10 or y < 10:
        return x * y

    # Calcula o tamanho dos números
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Divide os números em duas partes
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)

    # 3 chamadas recursivas
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)

    # Combina os resultados
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

a = 12345678
b = 87654321
print(karatsuba(a, b))