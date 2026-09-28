def _make_engine(self, engine='c'):
    if engine == 'c':
        self._engine = CParserWrapper(self.f, **self.options)
    else:
        if engine == 'python':
            klass = PythonParser
        elif engine == 'python-fwf':
            klass = FixedWidthFieldParser
        else:
            raise ValueError(f'Unknown engine: {engine} (valid options are "c", "python", or "python-fwf")')
        self._engine = klass(self.f, **self.options)