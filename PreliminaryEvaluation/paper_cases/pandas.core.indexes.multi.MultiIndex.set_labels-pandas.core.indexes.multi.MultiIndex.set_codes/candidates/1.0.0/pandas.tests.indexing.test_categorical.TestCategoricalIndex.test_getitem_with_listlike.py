def test_getitem_with_listlike(self):
    cats = Categorical([Timestamp('12-31-1999'), Timestamp('12-31-2000')])
    expected = DataFrame([[1, 0], [0, 1]], dtype='uint8', index=[0, 1], columns=cats)
    dummies = pd.get_dummies(cats)
    result = dummies[list(dummies.columns)]
    tm.assert_frame_equal(result, expected)