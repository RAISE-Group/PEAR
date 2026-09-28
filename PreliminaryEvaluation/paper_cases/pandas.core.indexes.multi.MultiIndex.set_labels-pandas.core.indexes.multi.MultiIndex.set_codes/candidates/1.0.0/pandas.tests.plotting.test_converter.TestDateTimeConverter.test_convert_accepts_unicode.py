def test_convert_accepts_unicode(self):
    r1 = self.dtc.convert('12:22', None, None)
    r2 = self.dtc.convert('12:22', None, None)
    assert r1 == r2, 'DatetimeConverter.convert should accept unicode'