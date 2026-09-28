def test_pivot_table_with_iterator_values(self):
    aggs = {'D': 'sum', 'E': 'mean'}
    pivot_values_list = pd.pivot_table(self.data, index=['A'], values=list(aggs.keys()), aggfunc=aggs)
    pivot_values_keys = pd.pivot_table(self.data, index=['A'], values=aggs.keys(), aggfunc=aggs)
    tm.assert_frame_equal(pivot_values_keys, pivot_values_list)
    agg_values_gen = (value for value in aggs.keys())
    pivot_values_gen = pd.pivot_table(self.data, index=['A'], values=agg_values_gen, aggfunc=aggs)
    tm.assert_frame_equal(pivot_values_gen, pivot_values_list)