def test_variable_labels(self):
    with StataReader(self.dta16_115) as rdr:
        sr_115 = rdr.variable_labels()
    with StataReader(self.dta16_117) as rdr:
        sr_117 = rdr.variable_labels()
    keys = ('var1', 'var2', 'var3')
    labels = ('label1', 'label2', 'label3')
    for k, v in sr_115.items():
        assert k in sr_117
        assert v == sr_117[k]
        assert k in keys
        assert v in labels