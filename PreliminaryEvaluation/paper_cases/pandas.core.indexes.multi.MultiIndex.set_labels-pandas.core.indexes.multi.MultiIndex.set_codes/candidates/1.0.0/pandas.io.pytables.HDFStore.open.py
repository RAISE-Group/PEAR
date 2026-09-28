def open(self, mode: str='a', **kwargs):
    """
        Open the file in the specified mode

        Parameters
        ----------
        mode : {'a', 'w', 'r', 'r+'}, default 'a'
            See HDFStore docstring or tables.open_file for info about modes
        """
    tables = _tables()
    if self._mode != mode:
        if self._mode in ['a', 'w'] and mode in ['r', 'r+']:
            pass
        elif mode in ['w']:
            if self.is_open:
                raise PossibleDataLossError(f'Re-opening the file [{self._path}] with mode [{self._mode}] will delete the current file!')
        self._mode = mode
    if self.is_open:
        self.close()
    if self._complevel and self._complevel > 0:
        self._filters = _tables().Filters(self._complevel, self._complib, fletcher32=self._fletcher32)
    try:
        self._handle = tables.open_file(self._path, self._mode, **kwargs)
    except IOError as err:
        if 'can not be written' in str(err):
            print(f'Opening {self._path} in read-only mode')
            self._handle = tables.open_file(self._path, 'r', **kwargs)
        else:
            raise
    except ValueError as err:
        if 'FILE_OPEN_POLICY' in str(err):
            hdf_version = tables.get_hdf5_version()
            err = ValueError(f'PyTables [{tables.__version__}] no longer supports opening multiple files\neven in read-only mode on this HDF5 version [{hdf_version}]. You can accept this\nand not open the same file multiple times at once,\nupgrade the HDF5 version, or downgrade to PyTables 3.0.0 which allows\nfiles to be opened multiple times at once\n')
        raise err
    except Exception as err:
        if self._mode == 'r' and 'Unable to open/create file' in str(err):
            raise IOError(str(err))
        raise