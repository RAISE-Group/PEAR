def test_constructor_coerce(self, mixed_index, float_index):
    self.check_coerce(mixed_index, Index([1.5, 2, 3, 4, 5]))
    self.check_coerce(float_index, Index(np.arange(5) * 2.5))
    self.check_coerce(float_index, Index(np.array(np.arange(5) * 2.5, dtype=object)))