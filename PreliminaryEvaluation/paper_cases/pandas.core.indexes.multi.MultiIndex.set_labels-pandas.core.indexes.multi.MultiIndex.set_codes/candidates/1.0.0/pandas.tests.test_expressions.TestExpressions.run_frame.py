def run_frame(self, df, other, run_binary=True):
    self.run_arithmetic(df, other)
    if run_binary:
        expr.set_use_numexpr(False)
        binary_comp = other + 1
        expr.set_use_numexpr(True)
        self.run_binary(df, binary_comp)
    for i in range(len(df.columns)):
        self.run_arithmetic(df.iloc[:, i], other.iloc[:, i])