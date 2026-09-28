def test_td64_op_nat_casting(self):
    ser = pd.Series(['NaT', 'NaT'], dtype='timedelta64[ns]')
    df = pd.DataFrame([[1, 2], [3, 4]])
    result = df * ser
    expected = pd.DataFrame({0: ser, 1: ser})
    tm.assert_frame_equal(result, expected)