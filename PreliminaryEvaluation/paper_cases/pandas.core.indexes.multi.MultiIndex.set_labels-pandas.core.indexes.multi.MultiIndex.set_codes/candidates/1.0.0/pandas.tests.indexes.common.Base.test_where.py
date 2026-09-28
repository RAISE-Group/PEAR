@pytest.mark.parametrize('klass', [list, tuple, np.array, Series])
def test_where(self, klass):
    i = self.create_index()
    cond = [True] * len(i)
    result = i.where(klass(cond))
    expected = i
    tm.assert_index_equal(result, expected)
    cond = [False] + [True] * len(i[1:])
    expected = pd.Index([i._na_value] + i[1:].tolist(), dtype=i.dtype)
    result = i.where(klass(cond))
    tm.assert_index_equal(result, expected)