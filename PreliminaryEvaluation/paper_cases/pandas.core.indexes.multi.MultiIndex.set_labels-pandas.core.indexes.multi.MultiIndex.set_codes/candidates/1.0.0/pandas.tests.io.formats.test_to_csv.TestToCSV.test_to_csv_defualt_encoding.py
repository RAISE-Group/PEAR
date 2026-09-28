def test_to_csv_defualt_encoding(self):
    df = DataFrame({'col': ['AAAAA', 'ÄÄÄÄÄ', 'ßßßßß', '聞聞聞聞聞']})
    with tm.ensure_clean('test.csv') as path:
        df.to_csv(path)
        tm.assert_frame_equal(pd.read_csv(path, index_col=0), df)