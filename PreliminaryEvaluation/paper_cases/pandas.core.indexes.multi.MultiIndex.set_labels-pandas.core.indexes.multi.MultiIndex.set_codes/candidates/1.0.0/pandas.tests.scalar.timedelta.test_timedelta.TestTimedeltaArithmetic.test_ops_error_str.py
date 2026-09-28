def test_ops_error_str(self):
    td = Timedelta('1 day')
    for left, right in [(td, 'a'), ('a', td)]:
        with pytest.raises(TypeError):
            left + right
        with pytest.raises(TypeError):
            left > right
        assert not left == right
        assert left != right