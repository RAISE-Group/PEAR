def test_append_dataframe_regression(self):
    df = pd.DataFrame({'A': [1, 2]})
    result = df.A.append([df])
    expected = pd.DataFrame({0: [1.0, 2.0, None, None], 'A': [None, None, 1.0, 2.0]}, index=[0, 1, 0, 1])
    tm.assert_frame_equal(expected, result)