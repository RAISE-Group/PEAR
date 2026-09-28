@pytest.mark.parametrize('dt64_series', [Series([Timestamp('19900315'), Timestamp('19900315')]), Series([pd.NaT, Timestamp('19900315')]), Series([pd.NaT, pd.NaT], dtype='datetime64[ns]')])
@pytest.mark.parametrize('one', [1, 1.0, np.array(1)])
def test_dt64_mul_div_numeric_invalid(self, one, dt64_series):
    msg = 'cannot perform .* with this index type'
    with pytest.raises(TypeError, match=msg):
        dt64_series * one
    with pytest.raises(TypeError, match=msg):
        one * dt64_series
    with pytest.raises(TypeError, match=msg):
        dt64_series / one
    with pytest.raises(TypeError, match=msg):
        one / dt64_series