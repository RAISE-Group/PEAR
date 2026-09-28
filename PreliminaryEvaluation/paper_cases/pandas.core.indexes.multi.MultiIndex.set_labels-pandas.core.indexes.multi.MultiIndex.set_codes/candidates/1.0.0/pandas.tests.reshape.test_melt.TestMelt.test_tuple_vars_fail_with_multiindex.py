def test_tuple_vars_fail_with_multiindex(self):
    tuple_a = ('A', 'a')
    list_a = [tuple_a]
    tuple_b = ('B', 'b')
    list_b = [tuple_b]
    msg = '(id|value)_vars must be a list of tuples when columns are a MultiIndex'
    for id_vars, value_vars in ((tuple_a, list_b), (list_a, tuple_b), (tuple_a, tuple_b)):
        with pytest.raises(ValueError, match=msg):
            self.df1.melt(id_vars=id_vars, value_vars=value_vars)