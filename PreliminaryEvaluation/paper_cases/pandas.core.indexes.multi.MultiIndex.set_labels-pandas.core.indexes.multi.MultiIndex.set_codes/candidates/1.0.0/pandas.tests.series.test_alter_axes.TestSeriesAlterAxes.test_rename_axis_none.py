@pytest.mark.parametrize('kwargs', [{'mapper': None}, {'index': None}, {}])
def test_rename_axis_none(self, kwargs):
    index = Index(list('abc'), name='foo')
    df = Series([1, 2, 3], index=index)
    result = df.rename_axis(**kwargs)
    expected_index = index.rename(None) if kwargs else index
    expected = Series([1, 2, 3], index=expected_index)
    tm.assert_series_equal(result, expected)