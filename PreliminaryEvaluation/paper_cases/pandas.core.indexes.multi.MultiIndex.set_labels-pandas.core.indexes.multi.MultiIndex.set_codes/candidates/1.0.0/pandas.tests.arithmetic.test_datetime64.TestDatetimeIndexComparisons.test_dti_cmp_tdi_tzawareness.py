@pytest.mark.parametrize('other', [pd.timedelta_range('1D', periods=10), pd.timedelta_range('1D', periods=10).to_series(), pd.timedelta_range('1D', periods=10).asi8.view('m8[ns]')], ids=lambda x: type(x).__name__)
def test_dti_cmp_tdi_tzawareness(self, other):
    dti = date_range('2000-01-01', periods=10, tz='Asia/Tokyo')
    result = dti == other
    expected = np.array([False] * 10)
    tm.assert_numpy_array_equal(result, expected)
    result = dti != other
    expected = np.array([True] * 10)
    tm.assert_numpy_array_equal(result, expected)
    msg = 'Invalid comparison between'
    with pytest.raises(TypeError, match=msg):
        dti < other
    with pytest.raises(TypeError, match=msg):
        dti <= other
    with pytest.raises(TypeError, match=msg):
        dti > other
    with pytest.raises(TypeError, match=msg):
        dti >= other