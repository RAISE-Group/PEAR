def test_rhs_alignment(self):

    def run_tests(df, rhs, right):
        lbl_one, idx_one, slice_one = (list('bcd'), [1, 2, 3], slice(1, 4))
        lbl_two, idx_two, slice_two = (['joe', 'jolie'], [1, 2], slice(1, 3))
        left = df.copy()
        left.loc[lbl_one, lbl_two] = rhs
        tm.assert_frame_equal(left, right)
        left = df.copy()
        left.iloc[idx_one, idx_two] = rhs
        tm.assert_frame_equal(left, right)
        left = df.copy()
        left.iloc[slice_one, slice_two] = rhs
        tm.assert_frame_equal(left, right)
    xs = np.arange(20).reshape(5, 4)
    cols = ['jim', 'joe', 'jolie', 'joline']
    df = DataFrame(xs, columns=cols, index=list('abcde'))
    rhs = -2 * df.iloc[3:0:-1, 2:0:-1]
    right = df.copy()
    right.iloc[1:4, 1:3] *= -2
    run_tests(df, rhs, right)
    for frame in [df, rhs, right]:
        frame['joe'] = frame['joe'].astype('float64')
        frame['jolie'] = frame['jolie'].map('@{0}'.format)
    run_tests(df, rhs, right)