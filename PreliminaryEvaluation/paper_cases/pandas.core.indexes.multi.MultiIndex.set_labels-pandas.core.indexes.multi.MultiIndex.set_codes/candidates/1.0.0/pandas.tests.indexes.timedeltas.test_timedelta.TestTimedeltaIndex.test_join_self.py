def test_join_self(self, join_type):
    index = timedelta_range('1 day', periods=10)
    joined = index.join(index, how=join_type)
    tm.assert_index_equal(index, joined)