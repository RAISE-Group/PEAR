@pytest.mark.parametrize('ts', [pd.Timestamp('2013-01-01'), pd.Timestamp('2013-01-01').to_pydatetime(), pd.Timestamp('2013-01-01').to_datetime64()])
def test_dt64arr_sub_dtscalar(self, box_with_array, ts):
    idx = pd.date_range('2013-01-01', periods=3)
    idx = tm.box_expected(idx, box_with_array)
    expected = pd.TimedeltaIndex(['0 Days', '1 Day', '2 Days'])
    expected = tm.box_expected(expected, box_with_array)
    result = idx - ts
    tm.assert_equal(result, expected)