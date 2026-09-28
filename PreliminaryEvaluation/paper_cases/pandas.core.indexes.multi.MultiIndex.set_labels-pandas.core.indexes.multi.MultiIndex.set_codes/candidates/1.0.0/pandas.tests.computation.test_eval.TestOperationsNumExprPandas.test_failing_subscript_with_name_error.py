def test_failing_subscript_with_name_error(self):
    df = DataFrame(np.random.randn(5, 3))
    with pytest.raises(NameError):
        self.eval('df[x > 2] > 2')