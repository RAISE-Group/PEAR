@pytest.mark.parametrize('klass', [list, tuple, np.array, pd.Series])
def test_where(self, klass):
    i = self.create_index()
    cond = [True] * len(i)
    expected = i
    result = i.where(klass(cond))
    tm.assert_index_equal(result, expected)
    cond = [False] + [True] * (len(i) - 1)
    expected = CategoricalIndex([np.nan] + i[1:].tolist(), categories=i.categories)
    result = i.where(klass(cond))
    tm.assert_index_equal(result, expected)