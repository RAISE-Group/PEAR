def test_apply_nanoseconds(self):
    tests = []
    tests.append((BusinessHour(), {Timestamp('2014-07-04 15:00') + Nano(5): Timestamp('2014-07-04 16:00') + Nano(5), Timestamp('2014-07-04 16:00') + Nano(5): Timestamp('2014-07-07 09:00') + Nano(5), Timestamp('2014-07-04 16:00') - Nano(5): Timestamp('2014-07-04 17:00') - Nano(5)}))
    tests.append((BusinessHour(-1), {Timestamp('2014-07-04 15:00') + Nano(5): Timestamp('2014-07-04 14:00') + Nano(5), Timestamp('2014-07-04 10:00') + Nano(5): Timestamp('2014-07-04 09:00') + Nano(5), Timestamp('2014-07-04 10:00') - Nano(5): Timestamp('2014-07-03 17:00') - Nano(5)}))
    for offset, cases in tests:
        for base, expected in cases.items():
            assert_offset_equal(offset, base, expected)