def test_join_self(self, join_type):
    index = date_range('1/1/2000', periods=10)
    joined = index.join(index, how=join_type)
    assert index is joined