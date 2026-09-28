@property
def _hasnans(self):
    """
        return if I have any nans; enables various perf speedups
        """
    return bool(self._isnan.any())