def test_margins_no_values_two_row_two_cols(self):
    self.data['D'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    result = self.data[['A', 'B', 'C', 'D']].pivot_table(index=['A', 'B'], columns=['C', 'D'], aggfunc=len, margins=True)
    assert result.All.tolist() == [3.0, 1.0, 4.0, 3.0, 11.0]