def test_applymap_subset_multiindex(self):

    def color_negative_red(val):
        """
            Takes a scalar and returns a string with
            the css property `'color: red'` for negative
            strings, black otherwise.
            """
        color = 'red' if val < 0 else 'black'
        return f'color: {color}'
    dic = {('a', 'd'): [-1.12, 2.11], ('a', 'c'): [2.78, -2.88], ('b', 'c'): [-3.99, 3.77], ('b', 'd'): [4.21, -1.22]}
    idx = pd.IndexSlice
    df = pd.DataFrame(dic, index=[0, 1])
    df.style.applymap(color_negative_red, subset=idx[:, idx['b', 'd']]).render()