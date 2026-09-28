def test_arith_flex_frame_raise(self, all_arithmetic_operators, float_frame):
    op = all_arithmetic_operators
    for dim in range(3, 6):
        arr = np.ones((1,) * dim)
        msg = 'Unable to coerce to Series/DataFrame'
        with pytest.raises(ValueError, match=msg):
            getattr(float_frame, op)(arr)