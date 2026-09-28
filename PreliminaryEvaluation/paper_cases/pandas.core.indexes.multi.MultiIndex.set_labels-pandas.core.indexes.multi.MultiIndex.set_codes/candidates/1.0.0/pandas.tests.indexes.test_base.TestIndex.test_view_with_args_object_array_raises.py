@pytest.mark.parametrize('index', ['unicode', 'string', pytest.param('categorical', marks=pytest.mark.xfail(reason='gh-25464')), 'bool', 'empty'], indirect=True)
def test_view_with_args_object_array_raises(self, index):
    msg = 'Cannot change data-type for object array'
    with pytest.raises(TypeError, match=msg):
        index.view('i8')