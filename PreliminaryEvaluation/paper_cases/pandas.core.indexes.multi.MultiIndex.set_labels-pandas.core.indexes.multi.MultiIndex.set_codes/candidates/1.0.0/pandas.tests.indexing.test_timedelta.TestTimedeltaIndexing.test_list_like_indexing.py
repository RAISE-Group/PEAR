@pytest.mark.parametrize('indexer, expected', [(0, [20, 1, 2, 3, 4, 5, 6, 7, 8, 9]), (slice(4, 8), [0, 1, 2, 3, 20, 20, 20, 20, 8, 9]), ([3, 5], [0, 1, 2, 20, 4, 20, 6, 7, 8, 9])])
def test_list_like_indexing(self, indexer, expected):
    df = pd.DataFrame({'x': range(10)}, dtype='int64')
    df.index = pd.to_timedelta(range(10), unit='s')
    df.loc[df.index[indexer], 'x'] = 20
    expected = pd.DataFrame(expected, index=pd.to_timedelta(range(10), unit='s'), columns=['x'], dtype='int64')
    tm.assert_frame_equal(expected, df)