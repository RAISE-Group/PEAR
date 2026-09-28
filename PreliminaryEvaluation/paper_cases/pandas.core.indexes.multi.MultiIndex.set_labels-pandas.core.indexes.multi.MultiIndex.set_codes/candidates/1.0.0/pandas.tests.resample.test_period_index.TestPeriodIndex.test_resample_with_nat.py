@pytest.mark.parametrize('periods, values', [([pd.NaT, '1970-01-01 00:00:00', pd.NaT, '1970-01-01 00:00:02', '1970-01-01 00:00:03'], [2, 3, 5, 7, 11]), ([pd.NaT, pd.NaT, '1970-01-01 00:00:00', pd.NaT, pd.NaT, pd.NaT, '1970-01-01 00:00:02', '1970-01-01 00:00:03', pd.NaT, pd.NaT], [1, 2, 3, 5, 6, 8, 7, 11, 12, 13])])
@pytest.mark.parametrize('freq, expected_values', [('1s', [3, np.NaN, 7, 11]), ('2s', [3, int((7 + 11) / 2)]), ('3s', [int((3 + 7) / 2), 11])])
def test_resample_with_nat(self, periods, values, freq, expected_values):
    index = PeriodIndex(periods, freq='S')
    frame = DataFrame(values, index=index)
    expected_index = period_range('1970-01-01 00:00:00', periods=len(expected_values), freq=freq)
    expected = DataFrame(expected_values, index=expected_index)
    result = frame.resample(freq).mean()
    tm.assert_frame_equal(result, expected)