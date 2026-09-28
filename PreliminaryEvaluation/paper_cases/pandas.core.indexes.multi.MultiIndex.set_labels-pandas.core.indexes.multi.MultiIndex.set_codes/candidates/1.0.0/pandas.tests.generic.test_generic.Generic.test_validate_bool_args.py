def test_validate_bool_args(self):
    df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    invalid_values = [1, 'True', [1, 2, 3], 5.0]
    for value in invalid_values:
        with pytest.raises(ValueError):
            super(DataFrame, df).rename_axis(mapper={'a': 'x', 'b': 'y'}, axis=1, inplace=value)
        with pytest.raises(ValueError):
            super(DataFrame, df).drop('a', axis=1, inplace=value)
        with pytest.raises(ValueError):
            super(DataFrame, df).sort_index(inplace=value)
        with pytest.raises(ValueError):
            super(DataFrame, df)._consolidate(inplace=value)
        with pytest.raises(ValueError):
            super(DataFrame, df).fillna(value=0, inplace=value)
        with pytest.raises(ValueError):
            super(DataFrame, df).replace(to_replace=1, value=7, inplace=value)
        with pytest.raises(ValueError):
            super(DataFrame, df).interpolate(inplace=value)
        with pytest.raises(ValueError):
            super(DataFrame, df)._where(cond=df.a > 2, inplace=value)
        with pytest.raises(ValueError):
            super(DataFrame, df).mask(cond=df.a > 2, inplace=value)