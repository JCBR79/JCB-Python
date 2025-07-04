def is_private_ip(ip_str):
    """
    Checks if a given IP address string is a private (LAN) IP addres.
    """
    try: 
        ip = ipaddress.ip_address(ip_str)
        return ip.is_private
    except ValueError:
        return False 