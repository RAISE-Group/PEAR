@pytest.mark.parametrize('level', [0, 'baz'])
def test_unstack_swaplevel_sortlevel(self, level):
    mi = pd.MultiIndex.from_product([[0], ['d', 'c']], names=['bar', 'baz'])
    df = pd.DataFrame([[0, 2], [1, 3]], index=mi, columns=['B', 'A'])
    df.columns.name = 'foo'
    expected = pd.DataFrame([[3, 1, 2, 0]], columns=pd.MultiIndex.from_tuples([('c', 'A'), ('c', 'B'), ('d', 'A'), ('d', 'B')], names=['baz', 'foo']))
    expected.index.name = 'bar'
    result = df.unstack().swaplevel(axis=1).sort_index(axis=1, level=level)
    tm.assert_frame_equal(result, expected)