def test_zero_step_raises(self):
    with pytest.raises(ValueError):
        BlockPlacement(slice(1, 1, 0))
    with pytest.raises(ValueError):
        BlockPlacement(slice(1, 2, 0))