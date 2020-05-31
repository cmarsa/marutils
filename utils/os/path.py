import os

def assert_path(path) -> str:
    '''
    Asserts if the specified path exists, if not
    it creates it. Creates the necessary directories
    if needed.

    arguments
    ---------
        path: a string containing the path to assert it's existance.

    returns
    -------
        path: returns the asserted path as a string.
    '''
    if (not os.path.exists(path)):
        os.makedirs(path)
    return path