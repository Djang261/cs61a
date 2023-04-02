def with_if_statement():
    """
    >>>result = with_if_statement()
    61A
    >>>print(resule)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def cond():
    return False

def true_func():
    print("Welcome to")
    return None

def false_func():
    print("61A")
    return None

result = with_if_statement()
print(result)
