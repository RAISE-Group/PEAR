def test_performance_warning_for_poor_alignment(self, engine, parser):
    df = DataFrame(randn(1000, 10))
    s = Series(randn(10000))
    if engine == 'numexpr':
        seen = PerformanceWarning
    else:
        seen = False
    with tm.assert_produces_warning(seen):
        pd.eval('df + s', engine=engine, parser=parser)
    s = Series(randn(1000))
    with tm.assert_produces_warning(False):
        pd.eval('df + s', engine=engine, parser=parser)
    df = DataFrame(randn(10, 10000))
    s = Series(randn(10000))
    with tm.assert_produces_warning(False):
        pd.eval('df + s', engine=engine, parser=parser)
    df = DataFrame(randn(10, 10))
    s = Series(randn(10000))
    is_python_engine = engine == 'python'
    if not is_python_engine:
        wrn = PerformanceWarning
    else:
        wrn = False
    with tm.assert_produces_warning(wrn) as w:
        pd.eval('df + s', engine=engine, parser=parser)
        if not is_python_engine:
            assert len(w) == 1
            msg = str(w[0].message)
            loged = np.log10(s.size - df.shape[1])
            expected = f"Alignment difference on axis 1 is larger than an order of magnitude on term 'df', by more than {loged:.4g}; performance may suffer"
            assert msg == expected