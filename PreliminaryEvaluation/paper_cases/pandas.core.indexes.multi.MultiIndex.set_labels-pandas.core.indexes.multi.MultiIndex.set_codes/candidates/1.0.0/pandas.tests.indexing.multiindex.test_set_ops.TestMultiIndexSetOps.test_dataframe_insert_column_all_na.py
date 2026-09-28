def test_dataframe_insert_column_all_na(self):
    mix = MultiIndex.from_tuples([('1a', '2a'), ('1a', '2b'), ('1a', '2c')])
    df = DataFrame([[1, 2], [3, 4], [5, 6]], index=mix)
    s = Series({(1, 1): 1, (1, 2): 2})
    df['new'] = s
    assert df['new'].isna().all()