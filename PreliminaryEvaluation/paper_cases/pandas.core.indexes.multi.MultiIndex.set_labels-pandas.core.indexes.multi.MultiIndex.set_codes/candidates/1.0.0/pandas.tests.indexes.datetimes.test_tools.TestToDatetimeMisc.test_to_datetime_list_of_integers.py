def test_to_datetime_list_of_integers(self):
    rng = date_range('1/1/2000', periods=20)
    rng = DatetimeIndex(rng.values)
    ints = list(rng.asi8)
    result = DatetimeIndex(ints)
    tm.assert_index_equal(rng, result)