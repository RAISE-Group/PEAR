@pytest.mark.parametrize('other', [1.0, np.array(1.0)])
def test_arithmetic_conversion(self, all_arithmetic_operators, other):
    op = self.get_op_from_name(all_arithmetic_operators)
    s = pd.Series([1, 2, 3], dtype='Int64')
    result = op(s, other)
    assert result.dtype is np.dtype('float')