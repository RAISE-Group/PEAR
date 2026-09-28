def test_argmax_axis_invalid(self):
    rng = self.create_index()
    with pytest.raises(ValueError):
        rng.argmax(axis=1)
    with pytest.raises(ValueError):
        rng.argmin(axis=2)
    with pytest.raises(ValueError):
        rng.min(axis=-2)
    with pytest.raises(ValueError):
        rng.max(axis=-3)