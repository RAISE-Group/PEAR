def __sizeof__(self):
    """
        Generates the total memory usage for an object that returns
        either a value or Series of values
        """
    if hasattr(self, 'memory_usage'):
        mem = self.memory_usage(deep=True)
        if not is_scalar(mem):
            mem = mem.sum()
        return int(mem)
    return super().__sizeof__()