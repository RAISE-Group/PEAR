def test_compare_frame_raises(self, all_compare_operators):
    op = getattr(operator, all_compare_operators)
    cat = Categorical(['a', 'b', 2, 'a'])
    df = DataFrame(cat)
    msg = 'Unable to coerce to Series, length must be 1: given 4'
    with pytest.raises(ValueError, match=msg):
        op(cat, df)