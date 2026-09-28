def diff(self, n: int, axis: int=1) -> List['Block']:
    if axis == 1:
        axis = 0
    return super().diff(n, axis)