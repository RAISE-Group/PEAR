@pytest.mark.parametrize('cat_data', [pd.Categorical(['a']), pd.Categorical([1]), pd.Series(pd.Categorical([1])), pd.CategoricalIndex([1]), pd.Categorical([1])])
def test_as_json_table_type_categorical_data(self, cat_data):
    assert as_json_table_type(cat_data) == 'any'