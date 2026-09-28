def update_kwargs(self, kwargs):
    kwargs = kwargs.copy()
    kwargs.update(dict(engine=self.engine, low_memory=self.low_memory))
    return kwargs