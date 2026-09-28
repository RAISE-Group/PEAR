@pytest.mark.parametrize('order', [['a', 'b', 'c'], ['c', 'b', 'a'], ['a'], ['b'], ['a', 'b'], ['c', 'b']])
@pytest.mark.parametrize('n', range(1, 6))
def test_nlargest_n_duplicate_index(self, df_duplicates, n, order):
    df = df_duplicates
    result = df.nsmallest(n, order)
    expected = df.sort_values(order).head(n)
    tm.assert_frame_equal(result, expected)
    result = df.nlargest(n, order)
    expected = df.sort_values(order, ascending=False).head(n)
    tm.assert_frame_equal(result, expected)