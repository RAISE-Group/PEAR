def test_constructor_no_data_string_type(self):
    result = pd.Series(index=[1], dtype=str)
    assert np.isnan(result.iloc[0])