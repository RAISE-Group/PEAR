@pytest.mark.parametrize('setter', ['loc', 'iloc'])
def test_setitem_scalar(self, data, setter):
    arr = pd.Series(data)
    setter = getattr(arr, setter)
    operator.setitem(setter, 0, data[1])
    assert arr[0] == data[1]