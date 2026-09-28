@pytest.mark.parametrize('other', [3.14, np.array([2.0, 3.0])])
@pytest.mark.parametrize('op', [operator.add, ops.radd, operator.sub, ops.rsub])
def test_parr_add_sub_float_raises(self, op, other, box_with_array):
    dti = pd.DatetimeIndex(['2011-01-01', '2011-01-02'], freq='D')
    pi = dti.to_period('D')
    pi = tm.box_expected(pi, box_with_array)
    with pytest.raises(TypeError):
        op(pi, other)