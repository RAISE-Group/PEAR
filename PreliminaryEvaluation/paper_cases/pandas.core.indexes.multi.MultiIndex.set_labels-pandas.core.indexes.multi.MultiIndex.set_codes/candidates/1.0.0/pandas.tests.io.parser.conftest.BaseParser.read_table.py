def read_table(self, *args, **kwargs):
    kwargs = self.update_kwargs(kwargs)
    return read_table(*args, **kwargs)