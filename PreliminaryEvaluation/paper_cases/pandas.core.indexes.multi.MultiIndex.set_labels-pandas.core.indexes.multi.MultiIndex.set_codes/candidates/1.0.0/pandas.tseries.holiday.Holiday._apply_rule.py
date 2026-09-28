def _apply_rule(self, dates):
    """
        Apply the given offset/observance to a DatetimeIndex of dates.

        Parameters
        ----------
        dates : DatetimeIndex
            Dates to apply the given offset/observance rule

        Returns
        -------
        Dates with rules applied
        """
    if self.observance is not None:
        return dates.map(lambda d: self.observance(d))
    if self.offset is not None:
        if not isinstance(self.offset, list):
            offsets = [self.offset]
        else:
            offsets = self.offset
        for offset in offsets:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', PerformanceWarning)
                dates += offset
    return dates