def test_coercion_with_setitem_and_dataframe(self):
    for start_data, expected_result in self.EXPECTED_SINGLE_ROW_RESULTS:
        start_dataframe = DataFrame({'foo': start_data})
        start_dataframe[start_dataframe['foo'] == start_dataframe['foo'][0]] = None
        expected_dataframe = DataFrame({'foo': expected_result})
        tm.assert_frame_equal(start_dataframe, expected_dataframe)