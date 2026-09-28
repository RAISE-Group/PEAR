def test_flex_method_subclass_metadata_preservation(self, all_arithmetic_operators):

    class MySeries(Series):
        _metadata = ['x']

        @property
        def _constructor(self):
            return MySeries
    opname = all_arithmetic_operators
    op = getattr(Series, opname)
    m = MySeries([1, 2, 3], name='test')
    m.x = 42
    result = op(m, 1)
    assert result.x == 42