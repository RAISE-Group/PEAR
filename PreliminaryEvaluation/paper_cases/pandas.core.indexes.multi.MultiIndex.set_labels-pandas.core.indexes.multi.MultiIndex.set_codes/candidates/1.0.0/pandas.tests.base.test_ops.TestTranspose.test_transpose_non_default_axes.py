def test_transpose_non_default_axes(self):
    for obj in self.objs:
        with pytest.raises(ValueError, match=self.errmsg):
            obj.transpose(1)
        with pytest.raises(ValueError, match=self.errmsg):
            obj.transpose(axes=1)