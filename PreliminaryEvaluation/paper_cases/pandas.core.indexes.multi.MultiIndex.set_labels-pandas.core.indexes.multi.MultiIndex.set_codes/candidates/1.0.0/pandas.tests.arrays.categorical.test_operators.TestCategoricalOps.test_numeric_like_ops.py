def test_numeric_like_ops(self):
    df = DataFrame({'value': np.random.randint(0, 10000, 100)})
    labels = ['{0} - {1}'.format(i, i + 499) for i in range(0, 10000, 500)]
    cat_labels = Categorical(labels, labels)
    df = df.sort_values(by=['value'], ascending=True)
    df['value_group'] = pd.cut(df.value, range(0, 10500, 500), right=False, labels=cat_labels)
    for op, str_rep in [('__add__', '\\+'), ('__sub__', '-'), ('__mul__', '\\*'), ('__truediv__', '/')]:
        msg = 'Series cannot perform the operation {}|unsupported operand'.format(str_rep)
        with pytest.raises(TypeError, match=msg):
            getattr(df, op)(df)
    s = df['value_group']
    for op in ['kurt', 'skew', 'var', 'std', 'mean', 'sum', 'median']:
        msg = 'Categorical cannot perform the operation {}'.format(op)
        with pytest.raises(TypeError, match=msg):
            getattr(s, op)(numeric_only=False)
    s = Series(Categorical([1, 2, 3, 4]))
    with pytest.raises(TypeError, match='Categorical cannot perform the operation sum'):
        np.sum(s)
    for op, str_rep in [('__add__', '\\+'), ('__sub__', '-'), ('__mul__', '\\*'), ('__truediv__', '/')]:
        msg = 'Series cannot perform the operation {}|unsupported operand'.format(str_rep)
        with pytest.raises(TypeError, match=msg):
            getattr(s, op)(2)
    msg = 'Object with dtype category cannot perform the numpy op log'
    with pytest.raises(TypeError, match=msg):
        np.log(s)