@Substitution(klass='GroupBy', versionadded='.. versionadded:: 0.21.0', examples=">>> df = pd.DataFrame({'A': 'a b a b'.split(), 'B': [1, 2, 3, 4]})\n>>> df\n   A  B\n0  a  1\n1  b  2\n2  a  3\n3  b  4\n\nTo get the difference between each groups maximum and minimum value in one\npass, you can do\n\n>>> df.groupby('A').pipe(lambda x: x.max() - x.min())\n   B\nA\na  2\nb  2")
@Appender(_pipe_template)
def pipe(self, func, *args, **kwargs):
    return com.pipe(self, func, *args, **kwargs)