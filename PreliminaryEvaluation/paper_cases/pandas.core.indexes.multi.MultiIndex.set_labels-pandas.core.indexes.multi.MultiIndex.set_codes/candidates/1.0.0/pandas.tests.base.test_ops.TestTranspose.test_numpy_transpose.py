def test_numpy_transpose(self):
    for obj in self.objs:
        tm.assert_equal(np.transpose(obj), obj)
        with pytest.raises(ValueError, match=self.errmsg):
            np.transpose(obj, axes=1)