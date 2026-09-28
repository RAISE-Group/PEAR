def test_invalid_delegation(self):
    self.Delegate._add_delegate_accessors(delegate=self.Delegator, accessors=self.Delegator._properties, typ='property')
    self.Delegate._add_delegate_accessors(delegate=self.Delegator, accessors=self.Delegator._methods, typ='method')
    delegate = self.Delegate(self.Delegator())
    with pytest.raises(TypeError):
        delegate.foo
    with pytest.raises(TypeError):
        delegate.foo = 5
    with pytest.raises(TypeError):
        delegate.foo()