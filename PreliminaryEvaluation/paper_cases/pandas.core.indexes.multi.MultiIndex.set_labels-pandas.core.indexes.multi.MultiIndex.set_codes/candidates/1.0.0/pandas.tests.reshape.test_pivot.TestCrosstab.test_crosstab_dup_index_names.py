def test_crosstab_dup_index_names(self):
    s = pd.Series(range(3), name='foo')
    result = pd.crosstab(s, s)
    expected_index = pd.Index(range(3), name='foo')
    expected = pd.DataFrame(np.eye(3, dtype=np.int64), index=expected_index, columns=expected_index)
    tm.assert_frame_equal(result, expected)