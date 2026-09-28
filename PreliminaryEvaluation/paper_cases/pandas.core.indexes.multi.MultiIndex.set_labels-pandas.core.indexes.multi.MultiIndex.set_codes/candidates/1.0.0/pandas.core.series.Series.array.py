@Appender(base.IndexOpsMixin.array.__doc__)
@property
def array(self) -> ExtensionArray:
    return self._data._block.array_values()