@Appender(IndexOpsMixin.memory_usage.__doc__)
def memory_usage(self, deep=False):
    result = super().memory_usage(deep=deep)
    result += self._engine.sizeof(deep=deep)
    return result