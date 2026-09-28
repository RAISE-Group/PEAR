@pytest.mark.parametrize('func,op_name', [(lambda idx: idx - idx, '__sub__'), (lambda idx: idx + idx, '__add__'), (lambda idx: idx - ['a', 'b'], '__sub__'), (lambda idx: idx + ['a', 'b'], '__add__'), (lambda idx: ['a', 'b'] - idx, '__rsub__'), (lambda idx: ['a', 'b'] + idx, '__radd__')])
def test_disallow_addsub_ops(self, func, op_name):
    idx = pd.Index(pd.Categorical(['a', 'b']))
    msg = f'cannot perform {op_name} with this index type: CategoricalIndex'
    with pytest.raises(TypeError, match=msg):
        func(idx)