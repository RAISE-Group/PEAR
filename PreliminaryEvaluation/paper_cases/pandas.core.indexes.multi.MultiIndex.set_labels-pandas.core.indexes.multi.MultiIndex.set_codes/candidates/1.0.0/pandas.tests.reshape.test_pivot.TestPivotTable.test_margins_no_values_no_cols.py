def test_margins_no_values_no_cols(self):
    result = self.data[['A', 'B']].pivot_table(index=['A', 'B'], aggfunc=len, margins=True)
    result_list = result.tolist()
    assert sum(result_list[:-1]) == result_list[-1]