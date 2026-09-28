@pytest.mark.parametrize('index', [Index(range(5)), tm.makeDateIndex(10), MultiIndex.from_tuples([('foo', '1'), ('bar', '3')]), period_range(start='2000', end='2010', freq='A')])
def test_str_attribute_raises(self, index):
    with pytest.raises(AttributeError, match='only use .str accessor'):
        index.str.repeat(2)