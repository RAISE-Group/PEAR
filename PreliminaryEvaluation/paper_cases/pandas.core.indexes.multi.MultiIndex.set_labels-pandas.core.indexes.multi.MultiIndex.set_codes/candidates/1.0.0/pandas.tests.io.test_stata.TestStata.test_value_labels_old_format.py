def test_value_labels_old_format(self):
    dpath = os.path.join(self.dirpath, 'S4_EDUC1.dta')
    reader = StataReader(dpath)
    assert reader.value_labels() == {}
    reader.close()