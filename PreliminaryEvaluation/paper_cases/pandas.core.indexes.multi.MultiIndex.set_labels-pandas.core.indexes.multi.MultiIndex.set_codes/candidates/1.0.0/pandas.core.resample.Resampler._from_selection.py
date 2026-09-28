@property
def _from_selection(self) -> bool:
    """
        Is the resampling from a DataFrame column or MultiIndex level.
        """
    return self.groupby is not None and (self.groupby.key is not None or self.groupby.level is not None)