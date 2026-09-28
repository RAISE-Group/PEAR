def test_frame_loc_callable_setitem(self):
    df = pd.DataFrame({'X': [1, 2, 3, 4], 'Y': list('aabb')}, index=list('ABCD'))
    res = df.copy()
    res.loc[lambda x: ['A', 'C']] = -20
    exp = df.copy()
    exp.loc[['A', 'C']] = -20
    tm.assert_frame_equal(res, exp)
    res = df.copy()
    res.loc[lambda x: ['A', 'C'], :] = 20
    exp = df.copy()
    exp.loc[['A', 'C'], :] = 20
    tm.assert_frame_equal(res, exp)
    res = df.copy()
    res.loc[lambda x: ['A', 'C'], lambda x: 'X'] = -1
    exp = df.copy()
    exp.loc[['A', 'C'], 'X'] = -1
    tm.assert_frame_equal(res, exp)
    res = df.copy()
    res.loc[lambda x: ['A', 'C'], lambda x: ['X']] = [5, 10]
    exp = df.copy()
    exp.loc[['A', 'C'], ['X']] = [5, 10]
    tm.assert_frame_equal(res, exp)
    res = df.copy()
    res.loc[['A', 'C'], lambda x: 'X'] = np.array([-1, -2])
    exp = df.copy()
    exp.loc[['A', 'C'], 'X'] = np.array([-1, -2])
    tm.assert_frame_equal(res, exp)
    res = df.copy()
    res.loc[['A', 'C'], lambda x: ['X']] = 10
    exp = df.copy()
    exp.loc[['A', 'C'], ['X']] = 10
    tm.assert_frame_equal(res, exp)
    res = df.copy()
    res.loc[lambda x: ['A', 'C'], 'X'] = -2
    exp = df.copy()
    exp.loc[['A', 'C'], 'X'] = -2
    tm.assert_frame_equal(res, exp)
    res = df.copy()
    res.loc[lambda x: ['A', 'C'], ['X']] = -4
    exp = df.copy()
    exp.loc[['A', 'C'], ['X']] = -4
    tm.assert_frame_equal(res, exp)