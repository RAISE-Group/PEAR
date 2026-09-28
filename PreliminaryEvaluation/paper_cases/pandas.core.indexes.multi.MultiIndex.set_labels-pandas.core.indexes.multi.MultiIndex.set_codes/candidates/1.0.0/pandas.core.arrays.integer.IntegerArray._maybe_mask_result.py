def _maybe_mask_result(self, result, mask, other, op_name):
    """
        Parameters
        ----------
        result : array-like
        mask : array-like bool
        other : scalar or array-like
        op_name : str
        """
    if (is_float_dtype(other) or is_float(other)) or op_name in ['rtruediv', 'truediv']:
        result[mask] = np.nan
        return result
    return type(self)(result, mask, copy=False)