def write(self, obj, **kwargs):
    """ we are going to write this as a frame table """
    name = obj.name or 'values'
    obj, self.levels = self.validate_multiindex(obj)
    cols = list(self.levels)
    cols.append(name)
    obj.columns = cols
    return super().write(obj=obj, **kwargs)