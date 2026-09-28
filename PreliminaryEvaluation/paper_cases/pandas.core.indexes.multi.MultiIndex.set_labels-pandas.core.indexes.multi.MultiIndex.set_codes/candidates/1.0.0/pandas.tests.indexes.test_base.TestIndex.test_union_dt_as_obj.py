@pytest.mark.parametrize('sort', [None, False])
def test_union_dt_as_obj(self, sort):
    index = self.create_index()
    date_index = pd.date_range('2019-01-01', periods=10)
    first_cat = index.union(date_index)
    second_cat = index.union(index)
    if date_index.dtype == np.object_:
        appended = np.append(index, date_index)
    else:
        appended = np.append(index, date_index.astype('O'))
    assert tm.equalContents(first_cat, appended)
    assert tm.equalContents(second_cat, index)
    tm.assert_contains_all(index, first_cat)
    tm.assert_contains_all(index, second_cat)
    tm.assert_contains_all(date_index, first_cat)