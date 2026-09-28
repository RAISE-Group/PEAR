def test_join_self(self, join_type):
    index = period_range('1/1/2000', '1/20/2000', freq='D')
    res = index.join(index, how=join_type)
    assert index is res