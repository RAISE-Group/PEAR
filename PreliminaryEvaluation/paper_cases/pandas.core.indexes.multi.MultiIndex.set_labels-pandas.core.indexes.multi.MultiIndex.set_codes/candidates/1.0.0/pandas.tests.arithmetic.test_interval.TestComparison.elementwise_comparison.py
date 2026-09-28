def elementwise_comparison(self, op, array, other):
    """
        Helper that performs elementwise comparisions between `array` and `other`
        """
    other = other if is_list_like(other) else [other] * len(array)
    return np.array([op(x, y) for x, y in zip(array, other)])