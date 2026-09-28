def test_concat_categorical_ordered(self):
    s1 = pd.Series(pd.Categorical([1, 2, np.nan], ordered=True))
    s2 = pd.Series(pd.Categorical([2, 1, 2], ordered=True))
    exp = pd.Series(pd.Categorical([1, 2, np.nan, 2, 1, 2], ordered=True))
    tm.assert_series_equal(pd.concat([s1, s2], ignore_index=True), exp)
    tm.assert_series_equal(s1.append(s2, ignore_index=True), exp)
    exp = pd.Series(pd.Categorical([1, 2, np.nan, 2, 1, 2, 1, 2, np.nan], ordered=True))
    tm.assert_series_equal(pd.concat([s1, s2, s1], ignore_index=True), exp)
    tm.assert_series_equal(s1.append([s2, s1], ignore_index=True), exp)