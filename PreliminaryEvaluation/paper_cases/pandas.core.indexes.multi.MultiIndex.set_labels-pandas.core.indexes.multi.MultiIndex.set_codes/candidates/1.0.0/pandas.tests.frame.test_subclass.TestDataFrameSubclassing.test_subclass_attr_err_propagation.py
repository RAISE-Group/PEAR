def test_subclass_attr_err_propagation(self):

    class A(DataFrame):

        @property
        def bar(self):
            return self.i_dont_exist
    with pytest.raises(AttributeError, match='.*i_dont_exist.*'):
        A().bar