@pytest.mark.xfail(reason='GH#27147 setitem changes underlying index')
def test_setitem_preserves_views(self, data):
    super().test_setitem_preserves_views(data)