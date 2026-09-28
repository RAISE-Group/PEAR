@classmethod
def _simple_new(cls, values, name=None, dtype=None):
    """
        We require that we have a dtype compat for the values. If we are passed
        a non-dtype compat, then coerce using the constructor.

        Must be careful not to recurse.
        """
    if isinstance(values, (ABCSeries, ABCIndexClass)):
        values = np.asarray(values._values)
    result = object.__new__(cls)
    result._data = values
    result._index_data = values
    result._name = name
    return result._reset_identity()