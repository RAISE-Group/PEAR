def test_setitem_empty(self):
    df = pd.DataFrame({'a': ['1', '2', '3'], 'b': ['11', '22', '33'], 'c': ['111', '222', '333']})
    result = df.copy()
    result.loc[result.b.isna(), 'a'] = result.a
    tm.assert_frame_equal(result, df)