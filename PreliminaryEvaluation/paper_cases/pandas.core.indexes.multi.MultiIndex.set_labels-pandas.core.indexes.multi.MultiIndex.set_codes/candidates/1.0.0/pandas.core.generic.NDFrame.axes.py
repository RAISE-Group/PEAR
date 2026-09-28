@property
def axes(self) -> List[Index]:
    """
        Return index label(s) of the internal NDFrame
        """
    return [self._get_axis(a) for a in self._AXIS_ORDERS]