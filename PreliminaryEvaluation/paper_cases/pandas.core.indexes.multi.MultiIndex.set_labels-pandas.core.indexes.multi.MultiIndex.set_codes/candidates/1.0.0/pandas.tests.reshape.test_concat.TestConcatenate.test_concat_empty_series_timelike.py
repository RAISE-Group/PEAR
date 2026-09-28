@pytest.mark.parametrize('tz', [None, 'UTC'])
@pytest.mark.parametrize('values', [[], [1, 2, 3]])
def test_concat_empty_series_timelike(self, tz, values):
    first = Series([], dtype='M8[ns]').dt.tz_localize(tz)
    dtype = None if values else np.float64
    second = Series(values, dtype=dtype)
    expected = DataFrame({0: pd.Series([pd.NaT] * len(values), dtype='M8[ns]').dt.tz_localize(tz), 1: values})
    result = concat([first, second], axis=1)
    tm.assert_frame_equal(result, expected)