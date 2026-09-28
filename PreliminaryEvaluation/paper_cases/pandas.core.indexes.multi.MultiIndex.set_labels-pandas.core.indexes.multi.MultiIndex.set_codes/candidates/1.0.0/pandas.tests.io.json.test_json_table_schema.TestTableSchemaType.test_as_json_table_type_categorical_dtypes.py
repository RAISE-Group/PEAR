def test_as_json_table_type_categorical_dtypes(self):
    assert as_json_table_type(pd.Categorical(['a'])) == 'any'
    assert as_json_table_type(CategoricalDtype()) == 'any'