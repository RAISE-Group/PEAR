def test_getitem_dupe_cols(self):
    df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'a', 'b'])
    msg = '"None of [Index([\'baf\'], dtype=\'object\')] are in the [columns]"'
    with pytest.raises(KeyError, match=re.escape(msg)):
        df[['baf']]