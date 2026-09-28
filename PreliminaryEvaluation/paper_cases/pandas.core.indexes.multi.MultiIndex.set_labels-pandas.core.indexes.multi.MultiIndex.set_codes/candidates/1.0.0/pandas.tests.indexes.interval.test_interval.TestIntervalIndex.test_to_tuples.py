@pytest.mark.parametrize('tuples', [list(zip(range(10), range(1, 11))), list(zip(date_range('20170101', periods=10), date_range('20170101', periods=10))), list(zip(timedelta_range('0 days', periods=10), timedelta_range('1 day', periods=10)))])
def test_to_tuples(self, tuples):
    idx = IntervalIndex.from_tuples(tuples)
    result = idx.to_tuples()
    expected = Index(com.asarray_tuplesafe(tuples))
    tm.assert_index_equal(result, expected)