@Appender(Index.memory_usage.__doc__)
def memory_usage(self, deep: bool=False) -> int:
    return self.left.memory_usage(deep=deep) + self.right.memory_usage(deep=deep)