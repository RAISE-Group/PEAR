def test_arith_len_mismatch(self, all_arithmetic_operators):
    op = self.get_op_from_name(all_arithmetic_operators)
    other = np.array([1.0])
    s = pd.Series([1, 2, 3], dtype='Int64')
    with pytest.raises(ValueError, match='Lengths must match'):
        op(s, other)