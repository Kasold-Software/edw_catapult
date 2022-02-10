import ctypes

ODBC_ADD_DSN = 1        # Add data source, user DSN only
ODBC_CONFIG_DSN = 2     # Configure (edit) data source
ODBC_REMOVE_DSN = 3     # Remove data source
ODBC_ADD_SYS_DSN = 4    # add a system DSN
ODBC_CONFIG_SYS_DSN = 5 # Configure a system DSN
ODBC_REMOVE_SYS_DSN = 6 # remove a system DSN

def add_dsn(name, driver, **kw):
    nul, attrib = '', []
    kw['DSN'] = name
    for attr, val in kw.items():
        attrib.append('%s=%s' % (attr, val))

    return ctypes.windll.ODBCCP32.SQLConfigDataSource(0, ODBC_ADD_DSN, driver, nul.join(attrib))

#
if __name__ == "__main__":
    print (add_dsn('test', 'SQL Server', server='ALPHA', description = 'Testing'))