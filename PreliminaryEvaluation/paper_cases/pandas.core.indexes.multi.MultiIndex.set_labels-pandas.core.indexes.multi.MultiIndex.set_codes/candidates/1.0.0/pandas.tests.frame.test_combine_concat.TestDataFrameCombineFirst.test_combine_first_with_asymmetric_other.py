@pytest.mark.parametrize('val', [1, 1.0])
def test_combine_first_with_asymmetric_other(self, val):
    df1 = pd.DataFrame({'isNum': [val]})
    df2 = pd.DataFrame({'isBool': [True]})
    res = df1.combine_first(df2)
    exp = pd.DataFrame({'isBool': [True], 'isNum': [val]})
    tm.assert_frame_equal(res, exp)