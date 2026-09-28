@pytest.mark.parametrize('op', ['+', '-', '*', '**', '/'])
@pytest.mark.parametrize('dt', [np.float32, np.float64])
def test_binop_typecasting(self, engine, parser, op, dt):
    df = tm.makeCustomDataframe(5, 3, data_gen_f=f, dtype=dt)
    s = f'df {op} 3'
    res = pd.eval(s, engine=engine, parser=parser)
    assert df.values.dtype == dt
    assert res.values.dtype == dt
    tm.assert_frame_equal(res, eval(s))
    s = f'3 {op} df'
    res = pd.eval(s, engine=engine, parser=parser)
    assert df.values.dtype == dt
    assert res.values.dtype == dt
    tm.assert_frame_equal(res, eval(s))