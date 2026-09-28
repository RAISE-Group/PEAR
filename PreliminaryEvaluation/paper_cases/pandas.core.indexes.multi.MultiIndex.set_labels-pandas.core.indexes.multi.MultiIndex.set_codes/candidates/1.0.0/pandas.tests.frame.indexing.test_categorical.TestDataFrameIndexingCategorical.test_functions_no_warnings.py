def test_functions_no_warnings(self):
    df = DataFrame({'value': np.random.randint(0, 100, 20)})
    labels = ['{0} - {1}'.format(i, i + 9) for i in range(0, 100, 10)]
    with tm.assert_produces_warning(False):
        df['group'] = pd.cut(df.value, range(0, 105, 10), right=False, labels=labels)