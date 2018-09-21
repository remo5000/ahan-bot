import socket

def get_ipv4(hostname):
    r"""Gets the ipv4 address of the given hostname. Some websites are only
    available via ipv6.

    Parameters
    ----------
    hostname : str

    Returns
    -------
    str
        ipv4 address of the given hostname

    Examples
    --------

    >>> get_ipv4('github.com')
    '192.30.253.113'
    """
    return socket.gethostbyname(hostname)
