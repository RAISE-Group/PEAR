def _check_iris_loaded_frame(self, iris_frame):
    pytype = iris_frame.dtypes[0].type
    row = iris_frame.iloc[0]
    assert issubclass(pytype, np.floating)
    tm.equalContents(row.values, [5.1, 3.5, 1.4, 0.2, 'Iris-setosa'])