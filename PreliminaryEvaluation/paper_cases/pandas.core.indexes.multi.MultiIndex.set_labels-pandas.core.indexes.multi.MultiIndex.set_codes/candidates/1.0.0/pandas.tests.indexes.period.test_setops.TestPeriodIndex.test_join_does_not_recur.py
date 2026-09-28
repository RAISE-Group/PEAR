def test_join_does_not_recur(self):
    df = tm.makeCustomDataframe(3, 2, data_gen_f=lambda *args: np.random.randint(2), c_idx_type='p', r_idx_type='dt')
    s = df.iloc[:2, 0]
    res = s.index.join(df.columns, how='outer')
    expected = Index([s.index[0], s.index[1], df.columns[0], df.columns[1]], object)
    tm.assert_index_equal(res, expected)