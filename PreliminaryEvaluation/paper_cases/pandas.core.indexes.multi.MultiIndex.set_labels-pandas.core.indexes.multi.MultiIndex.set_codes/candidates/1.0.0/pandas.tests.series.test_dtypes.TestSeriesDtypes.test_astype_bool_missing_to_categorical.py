def test_astype_bool_missing_to_categorical(self):
    s = Series([True, False, np.nan])
    assert s.dtypes == np.object_
    result = s.astype(CategoricalDtype(categories=[True, False]))
    expected = Series(Categorical([True, False, np.nan], categories=[True, False]))
    tm.assert_series_equal(result, expected)