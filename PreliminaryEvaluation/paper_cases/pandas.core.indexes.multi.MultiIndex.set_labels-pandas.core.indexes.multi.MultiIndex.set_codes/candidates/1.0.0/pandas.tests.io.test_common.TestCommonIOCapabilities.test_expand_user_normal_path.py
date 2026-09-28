def test_expand_user_normal_path(self):
    filename = '/somefolder/sometest'
    expanded_name = icom._expand_user(filename)
    assert expanded_name == filename
    assert os.path.expanduser(filename) == expanded_name