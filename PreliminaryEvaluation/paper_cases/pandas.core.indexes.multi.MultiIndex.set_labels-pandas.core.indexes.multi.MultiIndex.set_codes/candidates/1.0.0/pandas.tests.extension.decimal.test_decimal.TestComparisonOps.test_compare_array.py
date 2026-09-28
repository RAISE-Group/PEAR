def test_compare_array(self, data, all_compare_operators):
    op_name = all_compare_operators
    s = pd.Series(data)
    alter = np.random.choice([-1, 0, 1], len(data))
    other = pd.Series(data) * [decimal.Decimal(pow(2.0, i)) for i in alter]
    self._compare_other(s, data, op_name, other)