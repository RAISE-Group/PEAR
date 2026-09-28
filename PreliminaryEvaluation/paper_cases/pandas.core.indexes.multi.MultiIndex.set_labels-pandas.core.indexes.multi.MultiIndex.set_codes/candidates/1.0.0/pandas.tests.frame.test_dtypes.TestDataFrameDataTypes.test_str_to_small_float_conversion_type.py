def test_str_to_small_float_conversion_type(self):
    np.random.seed(13)
    col_data = [str(np.random.random() * 1e-12) for _ in range(5)]
    result = pd.DataFrame(col_data, columns=['A'])
    expected = pd.DataFrame(col_data, columns=['A'], dtype=object)
    tm.assert_frame_equal(result, expected)
    result.loc[result.index, 'A'] = [float(x) for x in col_data]
    expected = pd.DataFrame(col_data, columns=['A'], dtype=float)
    tm.assert_frame_equal(result, expected)