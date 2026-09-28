def test_to_csv_unicode_index_col(self):
    buf = StringIO('')
    df = DataFrame([['א', 'd2', 'd3', 'd4'], ['a1', 'a2', 'a3', 'a4']], columns=['א', 'ב', 'ג', 'ד'], index=['א', 'ב'])
    df.to_csv(buf, encoding='UTF-8')
    buf.seek(0)
    df2 = read_csv(buf, index_col=0, encoding='UTF-8')
    tm.assert_frame_equal(df, df2)