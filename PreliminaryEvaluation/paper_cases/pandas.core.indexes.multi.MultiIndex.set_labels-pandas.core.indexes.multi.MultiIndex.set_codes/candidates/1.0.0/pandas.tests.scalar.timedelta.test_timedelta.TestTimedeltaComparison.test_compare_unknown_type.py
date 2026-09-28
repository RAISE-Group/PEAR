@pytest.mark.parametrize('val', ['string', 1])
def test_compare_unknown_type(self, val):
    t = Timedelta('1s')
    with pytest.raises(TypeError):
        t >= val
    with pytest.raises(TypeError):
        t > val
    with pytest.raises(TypeError):
        t <= val
    with pytest.raises(TypeError):
        t < val