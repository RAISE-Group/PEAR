def test_view(self):
    i = self._holder([], name='Foo')
    i_view = i.view()
    assert i_view.name == 'Foo'
    i_view = i.view(self._dtype)
    tm.assert_index_equal(i, self._holder(i_view, name='Foo'))
    i_view = i.view(self._holder)
    tm.assert_index_equal(i, self._holder(i_view, name='Foo'))