@pytest.mark.parametrize('int_holder', [np.array, pd.Index])
@pytest.mark.parametrize('op', [operator.add, ops.radd])
def test_pi_add_intarray(self, int_holder, op):
    pi = pd.PeriodIndex([pd.Period('2015Q1'), pd.Period('NaT')])
    other = int_holder([4, -1])
    result = op(pi, other)
    expected = pd.PeriodIndex([pd.Period('2016Q1'), pd.Period('NaT')])
    tm.assert_index_equal(result, expected)