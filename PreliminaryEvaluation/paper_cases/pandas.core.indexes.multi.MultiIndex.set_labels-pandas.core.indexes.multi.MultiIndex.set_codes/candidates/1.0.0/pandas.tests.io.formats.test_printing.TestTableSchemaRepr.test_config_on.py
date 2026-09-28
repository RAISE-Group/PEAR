def test_config_on(self):
    df = pd.DataFrame({'A': [1, 2]})
    with pd.option_context('display.html.table_schema', True):
        result = df._repr_data_resource_()
    assert result is not None