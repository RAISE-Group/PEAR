def _check_expected_dtype(self, obj, label):
    """
        Check whether obj has expected dtype depending on label
        considering not-supported dtypes
        """
    if isinstance(obj, pd.Index):
        if label == 'bool':
            assert obj.dtype == 'object'
        else:
            assert obj.dtype == label
    elif isinstance(obj, pd.Series):
        if label.startswith('period'):
            assert obj.dtype == 'Period[M]'
        else:
            assert obj.dtype == label
    else:
        raise ValueError