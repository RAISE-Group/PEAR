@pytest.mark.parametrize('klass', [list, tuple, np.array, Series])
def test_where(self, klass):
    i = self.create_index()
    cond = [True] * len(i)
    expected = i
    result = i.where(klass(cond))
    cond = [False] + [True] * (len(i) - 1)
    expected = Float64Index([i._na_value] + i[1:].tolist())
    result = i.where(klass(cond))
    tm.assert_index_equal(result, expected)