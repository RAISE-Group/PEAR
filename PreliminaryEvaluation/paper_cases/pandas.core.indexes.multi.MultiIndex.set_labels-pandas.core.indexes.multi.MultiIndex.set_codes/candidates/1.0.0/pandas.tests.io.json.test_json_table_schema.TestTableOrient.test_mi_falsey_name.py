def test_mi_falsey_name(self):
    df = pd.DataFrame(np.random.randn(4, 4), index=pd.MultiIndex.from_product([('A', 'B'), ('a', 'b')]))
    result = [x['name'] for x in build_table_schema(df)['fields']]
    assert result == ['level_0', 'level_1', 0, 1, 2, 3]