def read_csv(self, *args, **kwargs):
    kwargs = self.update_kwargs(kwargs)
    return read_csv(*args, **kwargs)