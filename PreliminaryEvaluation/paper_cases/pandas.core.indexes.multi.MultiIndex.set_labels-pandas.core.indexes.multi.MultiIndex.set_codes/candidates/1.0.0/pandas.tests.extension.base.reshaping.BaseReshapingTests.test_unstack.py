@pytest.mark.parametrize('index', [pd.MultiIndex.from_product([['A', 'B'], ['a', 'b']], names=['a', 'b']), pd.MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('B', 'b')]), pd.MultiIndex.from_product([('A', 'B'), ('a', 'b', 'c'), (0, 1, 2)]), pd.MultiIndex.from_tuples([('A', 'a', 1), ('A', 'b', 0), ('A', 'a', 0), ('B', 'a', 0), ('B', 'c', 1)])])
@pytest.mark.parametrize('obj', ['series', 'frame'])
def test_unstack(self, data, index, obj):
    data = data[:len(index)]
    if obj == 'series':
        ser = pd.Series(data, index=index)
    else:
        ser = pd.DataFrame({'A': data, 'B': data}, index=index)
    n = index.nlevels
    levels = list(range(n))
    combinations = itertools.chain.from_iterable((itertools.permutations(levels, i) for i in range(1, n)))
    for level in combinations:
        result = ser.unstack(level=level)
        assert all((isinstance(result[col].array, type(data)) for col in result.columns))
        expected = ser.astype(object).unstack(level=level)
        result = result.astype(object)
        self.assert_frame_equal(result, expected)