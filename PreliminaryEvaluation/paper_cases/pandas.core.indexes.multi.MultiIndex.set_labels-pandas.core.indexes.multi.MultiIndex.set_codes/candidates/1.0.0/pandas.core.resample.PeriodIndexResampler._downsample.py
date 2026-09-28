def _downsample(self, how, **kwargs):
    """
        Downsample the cython defined function.

        Parameters
        ----------
        how : string / cython mapped function
        **kwargs : kw args passed to how function
        """
    if self.kind == 'timestamp':
        return super()._downsample(how, **kwargs)
    how = self._get_cython_func(how) or how
    ax = self.ax
    if is_subperiod(ax.freq, self.freq):
        return self._groupby_and_aggregate(how, grouper=self.grouper, **kwargs)
    elif is_superperiod(ax.freq, self.freq):
        if how == 'ohlc':
            return self._groupby_and_aggregate(how, grouper=self.grouper)
        return self.asfreq()
    elif ax.freq == self.freq:
        return self.asfreq()
    raise IncompatibleFrequency(f'Frequency {ax.freq} cannot be resampled to {self.freq}, as they are not sub or super periods')