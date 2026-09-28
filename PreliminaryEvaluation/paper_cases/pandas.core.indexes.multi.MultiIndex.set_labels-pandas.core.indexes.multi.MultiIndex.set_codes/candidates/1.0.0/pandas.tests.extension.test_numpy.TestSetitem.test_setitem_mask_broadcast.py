@skip_nested
@pytest.mark.parametrize('setter', ['loc', None])
def test_setitem_mask_broadcast(self, data, setter):
    super().test_setitem_mask_broadcast(data, setter)