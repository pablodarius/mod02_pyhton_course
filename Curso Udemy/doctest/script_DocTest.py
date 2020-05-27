def suma(a, b):
    """
    Esta función recibe dos parámetros y devuelve la suma de ambos
    para que salga aunque estén los test correctos, ejecutar con -v al final
    
    Pueden ser números:
    >>> suma(5,10)
    15

    >>> suma(0,0)
    0

    >>> suma(-5,7)
    2

    Pueden ser textos:
    >>> suma('aa','bb')
    'aabb'

    Pueden ser listas:
    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> suma(a,b)
    [1, 2, 3, 4, 5, 6]

    sumar distintos tipos:
    >>> suma(10, "hola")    
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    """
    return a+b

if __name__ == "__main__":
    import doctest
    doctest.testmod()