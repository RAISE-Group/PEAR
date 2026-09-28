@pytest.mark.parametrize('as_index', [True, False])
def test_groupby_extension_agg(self, as_index, data_for_grouping):
    df = pd.DataFrame({'A': [1, 1, 2, 2, 3, 3, 1, 4], 'B': data_for_grouping})
    result = df.groupby('B', as_index=as_index).A.mean()
    _, index = pd.factorize(data_for_grouping, sort=True)
    index = pd.Index(index, name='B')
    expected = pd.Series([3, 1, 4], index=index, name='A')
    if as_index:
        self.assert_series_equal(result, expected)
    else:
        expected = expected.reset_index()
        self.assert_frame_equal(result, expected)