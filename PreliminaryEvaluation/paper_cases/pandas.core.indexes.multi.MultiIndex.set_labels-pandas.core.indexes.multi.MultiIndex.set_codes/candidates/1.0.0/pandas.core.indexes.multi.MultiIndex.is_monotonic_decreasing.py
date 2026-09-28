@cache_readonly
def is_monotonic_decreasing(self) -> bool:
    """
        return if the index is monotonic decreasing (only equal or
        decreasing) values.
        """
    return self[::-1].is_monotonic_increasing