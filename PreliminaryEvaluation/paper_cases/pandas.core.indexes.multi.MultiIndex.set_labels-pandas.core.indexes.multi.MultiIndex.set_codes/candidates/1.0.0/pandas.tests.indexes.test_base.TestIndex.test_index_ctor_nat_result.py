@pytest.mark.parametrize('swap_objs', [True, False])
def test_index_ctor_nat_result(self, swap_objs):
    data = [np.datetime64('nat'), np.timedelta64('nat')]
    if swap_objs:
        data = data[::-1]
    expected = pd.Index(data, dtype=object)
    tm.assert_index_equal(Index(data), expected)
    tm.assert_index_equal(Index(np.array(data, dtype=object)), expected)