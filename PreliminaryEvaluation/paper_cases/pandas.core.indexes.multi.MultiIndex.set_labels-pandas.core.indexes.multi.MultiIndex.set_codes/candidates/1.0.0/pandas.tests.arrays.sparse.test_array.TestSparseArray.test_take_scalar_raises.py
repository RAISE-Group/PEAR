def test_take_scalar_raises(self):
    msg = "'indices' must be an array, not a scalar '2'."
    with pytest.raises(ValueError, match=msg):
        self.arr.take(2)