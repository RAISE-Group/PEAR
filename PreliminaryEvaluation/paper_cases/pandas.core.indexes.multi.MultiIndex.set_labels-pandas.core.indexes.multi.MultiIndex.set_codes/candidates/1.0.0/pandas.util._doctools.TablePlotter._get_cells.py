def _get_cells(self, left, right, vertical) -> Tuple[int, int]:
    """
        Calculate appropriate figure size based on left and right data.
        """
    if vertical:
        vcells = max(sum((self._shape(l)[0] for l in left)), self._shape(right)[0])
        hcells = max((self._shape(l)[1] for l in left)) + self._shape(right)[1]
    else:
        vcells = max([self._shape(l)[0] for l in left] + [self._shape(right)[0]])
        hcells = sum([self._shape(l)[1] for l in left] + [self._shape(right)[1]])
    return (hcells, vcells)