def if_integer(n):
    try:
        int(n)
        return True
    except ValueError:
        return False