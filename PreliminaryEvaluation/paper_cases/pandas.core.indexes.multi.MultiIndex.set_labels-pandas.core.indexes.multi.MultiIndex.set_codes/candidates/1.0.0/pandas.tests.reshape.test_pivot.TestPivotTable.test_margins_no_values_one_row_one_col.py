def test_margins_no_values_one_row_one_col(self):
    result = self.data[['A', 'B']].pivot_table(index='A', columns='B', aggfunc=len, margins=True)
    assert result.All.tolist() == [4.0, 7.0, 11.0]