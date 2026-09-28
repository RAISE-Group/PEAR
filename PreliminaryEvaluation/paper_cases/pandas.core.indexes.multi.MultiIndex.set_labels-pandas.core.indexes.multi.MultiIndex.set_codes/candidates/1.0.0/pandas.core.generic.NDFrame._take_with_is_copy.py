def _take_with_is_copy(self: FrameOrSeries, indices, axis=0, **kwargs) -> FrameOrSeries:
    """
        Internal version of the `take` method that sets the `_is_copy`
        attribute to keep track of the parent dataframe (using in indexing
        for the SettingWithCopyWarning).

        See the docstring of `take` for full explanation of the parameters.
        """
    result = self.take(indices=indices, axis=axis, **kwargs)
    if not result._get_axis(axis).equals(self._get_axis(axis)):
        result._set_is_copy(self)
    return result