def test_slice_with_zero_step_raises(self):
    s = Series(np.arange(20), index=_mklbl('A', 20))
    with pytest.raises(ValueError, match='slice step cannot be zero'):
        s[::0]
    with pytest.raises(ValueError, match='slice step cannot be zero'):
        s.loc[::0]