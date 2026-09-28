def test_copy_and_deepcopy(self):
    for shape in [0, 1, 2]:
        obj = self._construct(shape)
        for func in [copy, deepcopy, lambda x: x.copy(deep=False), lambda x: x.copy(deep=True)]:
            obj_copy = func(obj)
            assert obj_copy is not obj
            self._compare(obj_copy, obj)