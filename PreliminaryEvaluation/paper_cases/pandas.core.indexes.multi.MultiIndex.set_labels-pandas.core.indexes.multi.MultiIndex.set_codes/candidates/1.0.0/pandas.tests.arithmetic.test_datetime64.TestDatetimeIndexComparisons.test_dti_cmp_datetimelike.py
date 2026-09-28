@pytest.mark.parametrize('other', [datetime(2016, 1, 1), Timestamp('2016-01-01'), np.datetime64('2016-01-01')])
def test_dti_cmp_datetimelike(self, other, tz_naive_fixture):
    tz = tz_naive_fixture
    dti = pd.date_range('2016-01-01', periods=2, tz=tz)
    if tz is not None:
        if isinstance(other, np.datetime64):
            return
        other = localize_pydatetime(other, dti.tzinfo)
    result = dti == other
    expected = np.array([True, False])
    tm.assert_numpy_array_equal(result, expected)
    result = dti > other
    expected = np.array([False, True])
    tm.assert_numpy_array_equal(result, expected)
    result = dti >= other
    expected = np.array([True, True])
    tm.assert_numpy_array_equal(result, expected)
    result = dti < other
    expected = np.array([False, False])
    tm.assert_numpy_array_equal(result, expected)
    result = dti <= other
    expected = np.array([True, False])
    tm.assert_numpy_array_equal(result, expected)