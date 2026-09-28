def test_frame_from_json_precise_float(self):
    df = DataFrame([[4.56, 4.56, 4.56], [4.56, 4.56, 4.56]])
    result = read_json(df.to_json(), precise_float=True)
    tm.assert_frame_equal(result, df, check_index_type=False, check_column_type=False)