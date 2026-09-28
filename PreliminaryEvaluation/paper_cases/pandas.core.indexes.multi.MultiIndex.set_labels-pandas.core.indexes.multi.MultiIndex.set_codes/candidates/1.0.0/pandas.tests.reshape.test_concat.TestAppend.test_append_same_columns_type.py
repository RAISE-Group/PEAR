@pytest.mark.parametrize('index', all_indexes, ids=lambda x: type(x).__name__)
def test_append_same_columns_type(self, index):
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=index)
    ser_index = index[:2]
    ser = pd.Series([7, 8], index=ser_index, name=2)
    result = df.append(ser)
    expected = pd.DataFrame([[1.0, 2.0, 3.0], [4, 5, 6], [7, 8, np.nan]], index=[0, 1, 2], columns=index)
    tm.assert_frame_equal(result, expected)
    ser_index = index
    index = index[:2]
    df = pd.DataFrame([[1, 2], [4, 5]], columns=index)
    ser = pd.Series([7, 8, 9], index=ser_index, name=2)
    result = df.append(ser)
    expected = pd.DataFrame([[1, 2, np.nan], [4, 5, np.nan], [7, 8, 9]], index=[0, 1, 2], columns=ser_index)
    tm.assert_frame_equal(result, expected)