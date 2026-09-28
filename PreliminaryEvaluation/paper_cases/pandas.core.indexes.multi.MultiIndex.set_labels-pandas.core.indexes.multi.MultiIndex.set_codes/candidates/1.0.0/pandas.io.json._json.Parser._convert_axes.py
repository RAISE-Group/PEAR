def _convert_axes(self):
    """
        Try to convert axes.
        """
    for axis in self.obj._AXIS_NUMBERS.keys():
        new_axis, result = self._try_convert_data(axis, self.obj._get_axis(axis), use_dtypes=False, convert_dates=True)
        if result:
            setattr(self.obj, axis, new_axis)