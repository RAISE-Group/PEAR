def test_encode_non_c_locale(self):
    lc_category = locale.LC_NUMERIC
    for new_locale in ('it_IT.UTF-8', 'Italian_Italy'):
        if tm.can_set_locale(new_locale, lc_category):
            with tm.set_locale(new_locale, lc_category):
                assert ujson.loads(ujson.dumps(4.78e+60)) == 4.78e+60
                assert ujson.loads('4.78', precise_float=True) == 4.78
            break