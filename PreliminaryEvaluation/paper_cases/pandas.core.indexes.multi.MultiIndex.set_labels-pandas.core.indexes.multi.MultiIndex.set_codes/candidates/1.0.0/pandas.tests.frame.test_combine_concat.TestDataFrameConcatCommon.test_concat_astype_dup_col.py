def test_concat_astype_dup_col(self):
    df = pd.DataFrame([{'a': 'b'}])
    df = pd.concat([df, df], axis=1)
    result = df.astype('category')
    expected = pd.DataFrame(np.array(['b', 'b']).reshape(1, 2), columns=['a', 'a']).astype('category')
    tm.assert_frame_equal(result, expected)