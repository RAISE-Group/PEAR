@pytest.mark.parametrize('freq', ['H', 'D'])
@pytest.mark.parametrize('int_holder', [np.array, pd.Index])
def test_dti_add_intarray_tick(self, int_holder, freq):
    dti = pd.date_range('2016-01-01', periods=2, freq=freq)
    other = int_holder([4, -1])
    msg = 'Addition/subtraction of integers|cannot subtract DatetimeArray from'
    assert_invalid_addsub_type(dti, other, msg)