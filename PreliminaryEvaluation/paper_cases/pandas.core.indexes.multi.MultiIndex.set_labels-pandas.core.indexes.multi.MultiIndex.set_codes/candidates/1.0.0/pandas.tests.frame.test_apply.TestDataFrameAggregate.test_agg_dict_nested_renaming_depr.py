def test_agg_dict_nested_renaming_depr(self):
    df = pd.DataFrame({'A': range(5), 'B': 5})
    msg = 'nested renamer is not supported'
    with pytest.raises(SpecificationError, match=msg):
        df.agg({'A': {'foo': 'min'}, 'B': {'bar': 'max'}})