def test_comparison_invalid(self, tz_naive_fixture, box_with_array):
    tz = tz_naive_fixture
    ser = Series(range(5))
    ser2 = Series(pd.date_range('20010101', periods=5, tz=tz))
    ser = tm.box_expected(ser, box_with_array)
    ser2 = tm.box_expected(ser2, box_with_array)
    assert_invalid_comparison(ser, ser2, box_with_array)