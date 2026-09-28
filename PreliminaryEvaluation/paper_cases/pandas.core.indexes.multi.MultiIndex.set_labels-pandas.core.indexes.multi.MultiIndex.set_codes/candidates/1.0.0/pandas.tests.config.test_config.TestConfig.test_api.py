def test_api(self):
    assert hasattr(pd, 'get_option')
    assert hasattr(pd, 'set_option')
    assert hasattr(pd, 'reset_option')
    assert hasattr(pd, 'describe_option')