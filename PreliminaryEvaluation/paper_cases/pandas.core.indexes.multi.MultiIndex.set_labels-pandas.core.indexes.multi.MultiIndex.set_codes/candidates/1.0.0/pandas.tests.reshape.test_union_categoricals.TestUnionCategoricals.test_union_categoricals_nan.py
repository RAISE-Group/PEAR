def test_union_categoricals_nan(self):
    res = union_categoricals([pd.Categorical([1, 2, np.nan]), pd.Categorical([3, 2, np.nan])])
    exp = Categorical([1, 2, np.nan, 3, 2, np.nan])
    tm.assert_categorical_equal(res, exp)
    res = union_categoricals([pd.Categorical(['A', 'B']), pd.Categorical(['B', 'B', np.nan])])
    exp = Categorical(['A', 'B', 'B', 'B', np.nan])
    tm.assert_categorical_equal(res, exp)
    val1 = [pd.Timestamp('2011-01-01'), pd.Timestamp('2011-03-01'), pd.NaT]
    val2 = [pd.NaT, pd.Timestamp('2011-01-01'), pd.Timestamp('2011-02-01')]
    res = union_categoricals([pd.Categorical(val1), pd.Categorical(val2)])
    exp = Categorical(val1 + val2, categories=[pd.Timestamp('2011-01-01'), pd.Timestamp('2011-03-01'), pd.Timestamp('2011-02-01')])
    tm.assert_categorical_equal(res, exp)
    res = union_categoricals([pd.Categorical(np.array([np.nan, np.nan], dtype=object)), pd.Categorical(['X'])])
    exp = Categorical([np.nan, np.nan, 'X'])
    tm.assert_categorical_equal(res, exp)
    res = union_categoricals([pd.Categorical([np.nan, np.nan]), pd.Categorical([np.nan, np.nan])])
    exp = Categorical([np.nan, np.nan, np.nan, np.nan])
    tm.assert_categorical_equal(res, exp)