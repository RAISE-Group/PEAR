@classmethod
def _validate_frequency(cls, index, freq, **kwargs):
    """
        Validate that a frequency is compatible with the values of a given
        Datetime Array/Index or Timedelta Array/Index

        Parameters
        ----------
        index : DatetimeIndex or TimedeltaIndex
            The index on which to determine if the given frequency is valid
        freq : DateOffset
            The frequency to validate
        """
    if is_period_dtype(cls):
        return None
    inferred = index.inferred_freq
    if index.size == 0 or inferred == freq.freqstr:
        return None
    try:
        on_freq = cls._generate_range(start=index[0], end=None, periods=len(index), freq=freq, **kwargs)
        if not np.array_equal(index.asi8, on_freq.asi8):
            raise ValueError
    except ValueError as e:
        if 'non-fixed' in str(e):
            raise e
        raise ValueError(f'Inferred frequency {inferred} from passed values does not conform to passed frequency {freq.freqstr}')