def test_loc_non_unique_memory_error(self):
    columns = list('ABCDEFG')

    def gen_test(l, l2):
        return pd.concat([DataFrame(np.random.randn(l, len(columns)), index=np.arange(l), columns=columns), DataFrame(np.ones((l2, len(columns))), index=[0] * l2, columns=columns)])

    def gen_expected(df, mask):
        len_mask = len(mask)
        return pd.concat([df.take([0]), DataFrame(np.ones((len_mask, len(columns))), index=[0] * len_mask, columns=columns), df.take(mask[1:])])
    df = gen_test(900, 100)
    assert df.index.is_unique is False
    mask = np.arange(100)
    result = df.loc[mask]
    expected = gen_expected(df, mask)
    tm.assert_frame_equal(result, expected)
    df = gen_test(900000, 100000)
    assert df.index.is_unique is False
    mask = np.arange(100000)
    result = df.loc[mask]
    expected = gen_expected(df, mask)
    tm.assert_frame_equal(result, expected)