def test_is_mixed_dtype(self):
    assert not create_mgr('a,b:f8').is_mixed_type
    assert not create_mgr('a:f8-1; b:f8-2').is_mixed_type
    assert create_mgr('a,b:f8; c,d: f4').is_mixed_type
    assert create_mgr('a,b:f8; c,d: object').is_mixed_type