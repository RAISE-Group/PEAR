def test_astype_object_with_nat(self):
    idx = TimedeltaIndex([timedelta(days=1), timedelta(days=2), NaT, timedelta(days=4)], name='idx')
    expected_list = [Timedelta('1 days'), Timedelta('2 days'), NaT, Timedelta('4 days')]
    result = idx.astype(object)
    expected = Index(expected_list, dtype=object, name='idx')
    tm.assert_index_equal(result, expected)
    assert idx.tolist() == expected_list