def test_unicode_repr_doesnt_raise(self):
    repr(create_mgr('b,א: object'))