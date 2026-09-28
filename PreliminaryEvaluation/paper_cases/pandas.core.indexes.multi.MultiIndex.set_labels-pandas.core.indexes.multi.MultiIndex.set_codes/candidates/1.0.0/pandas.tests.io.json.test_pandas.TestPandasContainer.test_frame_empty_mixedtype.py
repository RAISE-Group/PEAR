def test_frame_empty_mixedtype(self):
    df = DataFrame(columns=['jim', 'joe'])
    df['joe'] = df['joe'].astype('i8')
    assert df._is_mixed_type
    tm.assert_frame_equal(read_json(df.to_json(), dtype=dict(df.dtypes)), df, check_index_type=False)