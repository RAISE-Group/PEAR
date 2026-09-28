@pytest.mark.parametrize('columns', [['A', 'B'], pd.MultiIndex.from_tuples([('A', 'a'), ('A', 'b')], names=['outer', 'inner'])])
def test_stack(self, data, columns):
    df = pd.DataFrame({'A': data[:5], 'B': data[:5]})
    df.columns = columns
    result = df.stack()
    expected = df.astype(object).stack()
    expected = expected.astype(object)
    if isinstance(expected, pd.Series):
        assert result.dtype == df.iloc[:, 0].dtype
    else:
        assert all(result.dtypes == df.iloc[:, 0].dtype)
    result = result.astype(object)
    self.assert_equal(result, expected)