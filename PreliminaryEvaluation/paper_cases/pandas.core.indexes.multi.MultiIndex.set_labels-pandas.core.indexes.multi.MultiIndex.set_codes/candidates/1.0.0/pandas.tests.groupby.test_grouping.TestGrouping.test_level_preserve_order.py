@pytest.mark.parametrize('sort,labels', [[True, [2, 2, 2, 0, 0, 1, 1, 3, 3, 3]], [False, [0, 0, 0, 1, 1, 2, 2, 3, 3, 3]]])
def test_level_preserve_order(self, sort, labels, mframe):
    grouped = mframe.groupby(level=0, sort=sort)
    exp_labels = np.array(labels, np.intp)
    tm.assert_almost_equal(grouped.grouper.codes[0], exp_labels)