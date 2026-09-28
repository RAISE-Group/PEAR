def check_mutable_error(self, *args, **kwargs):
    mutable_regex = re.compile('does not support mutable operations')
    with pytest.raises(TypeError):
        mutable_regex(*args, **kwargs)