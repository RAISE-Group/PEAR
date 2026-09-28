@Appender(Index.memory_usage.__doc__)
def memory_usage(self, deep: bool=False) -> int:
    return self._nbytes(deep)