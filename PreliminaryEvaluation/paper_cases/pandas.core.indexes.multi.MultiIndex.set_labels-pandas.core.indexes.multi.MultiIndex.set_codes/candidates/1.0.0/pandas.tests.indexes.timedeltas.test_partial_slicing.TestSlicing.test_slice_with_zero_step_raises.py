def test_slice_with_zero_step_raises(self):
    ts = Series(np.arange(20), timedelta_range('0', periods=20, freq='H'))
    with pytest.raises(ValueError, match='slice step cannot be zero'):
        ts[::0]
    with pytest.raises(ValueError, match='slice step cannot be zero'):
        ts.loc[::0]
    with pytest.raises(ValueError, match='slice step cannot be zero'):
        ts.loc[::0]