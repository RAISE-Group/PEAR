@pytest.mark.parametrize('tz', [None, 'UTC'])
def test_diff_datetime_axis1(self, tz):
    df = DataFrame({0: date_range('2010', freq='D', periods=2, tz=tz), 1: date_range('2010', freq='D', periods=2, tz=tz)})
    if tz is None:
        result = df.diff(axis=1)
        expected = DataFrame({0: pd.TimedeltaIndex(['NaT', 'NaT']), 1: pd.TimedeltaIndex(['0 days', '0 days'])})
        tm.assert_frame_equal(result, expected)
    else:
        with pytest.raises(NotImplementedError):
            result = df.diff(axis=1)