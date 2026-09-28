@pytest.mark.parametrize('int_holder', [np.array, pd.Index])
def test_pi_sub_intarray(self, int_holder):
    pi = pd.PeriodIndex([pd.Period('2015Q1'), pd.Period('NaT')])
    other = int_holder([4, -1])
    result = pi - other
    expected = pd.PeriodIndex([pd.Period('2014Q1'), pd.Period('NaT')])
    tm.assert_index_equal(result, expected)
    with pytest.raises(TypeError):
        other - pi