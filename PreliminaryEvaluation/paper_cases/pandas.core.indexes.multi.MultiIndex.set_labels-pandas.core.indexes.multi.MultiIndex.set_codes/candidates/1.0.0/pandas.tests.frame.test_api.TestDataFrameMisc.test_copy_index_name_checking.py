def test_copy_index_name_checking(self, float_frame):
    for attr in ('index', 'columns'):
        ind = getattr(float_frame, attr)
        ind.name = None
        cp = float_frame.copy()
        getattr(cp, attr).name = 'foo'
        assert getattr(float_frame, attr).name is None