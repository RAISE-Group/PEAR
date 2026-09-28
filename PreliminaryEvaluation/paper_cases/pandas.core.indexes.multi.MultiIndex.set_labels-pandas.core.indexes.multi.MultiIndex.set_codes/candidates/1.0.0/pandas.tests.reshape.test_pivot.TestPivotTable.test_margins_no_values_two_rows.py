def test_margins_no_values_two_rows(self):
    result = self.data[['A', 'B', 'C']].pivot_table(index=['A', 'B'], columns='C', aggfunc=len, margins=True)
    assert result.All.tolist() == [3.0, 1.0, 4.0, 3.0, 11.0]