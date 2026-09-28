def get_value(self, name, f, i, values=False):
    """ return the value for the location i """
    if values:
        return f.values[i]
    elif name == 'iat':
        return f.iloc[i]
    else:
        assert name == 'at'
        return f.loc[i]