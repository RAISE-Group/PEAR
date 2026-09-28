def test_dt64arr_iadd_timedeltalike_scalar(self, tz_naive_fixture, two_hours, box_with_array):
    tz = tz_naive_fixture
    rng = pd.date_range('2000-01-01', '2000-02-01', tz=tz)
    expected = pd.date_range('2000-01-01 02:00', '2000-02-01 02:00', tz=tz)
    rng = tm.box_expected(rng, box_with_array)
    expected = tm.box_expected(expected, box_with_array)
    rng += two_hours
    tm.assert_equal(rng, expected)