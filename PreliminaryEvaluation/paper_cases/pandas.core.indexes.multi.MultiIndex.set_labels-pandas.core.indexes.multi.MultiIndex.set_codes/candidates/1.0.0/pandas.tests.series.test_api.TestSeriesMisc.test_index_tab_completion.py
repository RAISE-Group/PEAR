@pytest.mark.parametrize('index', [tm.makeUnicodeIndex(10), tm.makeStringIndex(10), tm.makeCategoricalIndex(10), Index(['foo', 'bar', 'baz'] * 2), tm.makeDateIndex(10), tm.makePeriodIndex(10), tm.makeTimedeltaIndex(10), tm.makeIntIndex(10), tm.makeUIntIndex(10), tm.makeIntIndex(10), tm.makeFloatIndex(10), Index([True, False]), Index(['a{}'.format(i) for i in range(101)]), pd.MultiIndex.from_tuples(zip('ABCD', 'EFGH')), pd.MultiIndex.from_tuples(zip([0, 1, 2, 3], 'EFGH'))])
def test_index_tab_completion(self, index):
    s = pd.Series(index=index, dtype=object)
    dir_s = dir(s)
    for i, x in enumerate(s.index.unique(level=0)):
        if i < 100:
            assert not isinstance(x, str) or not x.isidentifier() or x in dir_s
        else:
            assert x not in dir_s