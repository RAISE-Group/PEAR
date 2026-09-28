def rollforward(self, dt):
    """
        Roll provided date forward to next offset only if not on offset.

        Returns
        -------
        TimeStamp
            Rolled timestamp if not on offset, otherwise unchanged timestamp.
        """
    dt = as_timestamp(dt)
    if not self.is_on_offset(dt):
        dt = dt + type(self)(1, normalize=self.normalize, **self.kwds)
    return dt