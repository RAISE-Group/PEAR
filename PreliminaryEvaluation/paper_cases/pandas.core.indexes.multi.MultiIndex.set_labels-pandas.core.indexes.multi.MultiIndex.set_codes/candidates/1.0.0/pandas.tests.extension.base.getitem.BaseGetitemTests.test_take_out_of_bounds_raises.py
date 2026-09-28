@pytest.mark.parametrize('allow_fill', [True, False])
def test_take_out_of_bounds_raises(self, data, allow_fill):
    arr = data[:3]
    with pytest.raises(IndexError):
        arr.take(np.asarray([0, 3]), allow_fill=allow_fill)