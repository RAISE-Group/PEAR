def test_mutated(self):
    msg = "groupby\\(\\) got an unexpected keyword argument 'foo'"
    with pytest.raises(TypeError, match=msg):
        self.frame.groupby('A', foo=1)
    g = self.frame.groupby('A')
    assert not g.mutated
    g = get_groupby(self.frame, by='A', mutated=True)
    assert g.mutated