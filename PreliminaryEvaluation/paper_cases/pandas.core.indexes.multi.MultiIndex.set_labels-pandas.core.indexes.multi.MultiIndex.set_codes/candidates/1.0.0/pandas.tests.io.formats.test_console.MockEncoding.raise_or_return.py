@staticmethod
def raise_or_return(val):
    if isinstance(val, str):
        return val
    else:
        raise val