def test_class_axis(self):
    assert pydoc.getdoc(DataFrame.index)
    assert pydoc.getdoc(DataFrame.columns)