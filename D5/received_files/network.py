import ipaddress

def validate_ip_and_subnet(ip_string, subnet_string):
    """
    Validates an IP address and a subnet using the ipaddress module.

    Args:
        ip_string (str): The IP address to validate (e.g., "192.168.1.1").
        subnet_string (str): The subnet to validate (e.g., "192.168.1.0/24").

    Returns:
        tuple: A tuple containing booleans (is_ip_valid, is_subnet_valid).
               If valid, it also returns the ipaddress objects; otherwise, None.
    """
    is_ip_valid = False
    ip_object = None
    is_subnet_valid = False
    subnet_object = None

    try:
        ip_object = ipaddress.ip_address(ip_string)
        is_ip_valid = True
    except ValueError:
        print(f"Error: '{ip_string}' is not a valid IP address.")

    try:
        subnet_object = ipaddress.ip_network(subnet_string, strict=False)
        is_subnet_valid = True
    except ValueError:
        print(f"Error: '{subnet_string}' is not a valid subnet.")

    return is_ip_valid, ip_object, is_subnet_valid, subnet_object

# --- Examples ---

# Valid cases
print("--- Valid Cases ---")
ip_str_valid = "192.168.1.100"
subnet_str_valid_ipv4 = "192.168.1.0/24"
subnet_str_valid_ipv6 = "2001:db8::/32"

is_ip_v, ip_obj_v, is_subnet_v, subnet_obj_v = validate_ip_and_subnet(ip_str_valid, subnet_str_valid_ipv4)
if is_ip_v:
    print(f"IP '{ip_str_valid}' is valid. IP object: {ip_obj_v}")
if is_subnet_v:
    print(f"Subnet '{subnet_str_valid_ipv4}' is valid. Subnet object: {subnet_obj_v}")

ip_str_valid_ipv6 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
is_ip_v6, ip_obj_v6, is_subnet_v6, subnet_obj_v6 = validate_ip_and_subnet(ip_str_valid_ipv6, subnet_str_valid_ipv6)
if is_ip_v6:
    print(f"IP '{ip_str_valid_ipv6}' is valid. IP object: {ip_obj_v6}")
if is_subnet_v6:
    print(f"Subnet '{subnet_str_valid_ipv6}' is valid. Subnet object: {subnet_obj_v6}")


# Invalid cases
print("\n--- Invalid Cases ---")
ip_str_invalid = "256.0.0.1"  # Invalid IP address
subnet_str_invalid = "192.168.1.0/33"  # Invalid subnet mask

is_ip_iv, ip_obj_iv, is_subnet_iv, subnet_obj_iv = validate_ip_and_subnet(ip_str_invalid, subnet_str_invalid)
if not is_ip_iv:
    print(f"IP '{ip_str_invalid}' is invalid as expected.")
if not is_subnet_iv:
    print(f"Subnet '{subnet_str_invalid}' is invalid as expected.")

ip_str_malformed = "not_an_ip"
subnet_str_malformed = "not_a_subnet"
validate_ip_and_subnet(ip_str_malformed, subnet_str_malformed)

# Example of checking if an IP is within a subnet
print("\n--- IP in Subnet Check ---")
ip_to_check = "192.168.1.50"
subnet_to_check = "192.168.1.0/24"

is_ip, ip_obj_check, is_subnet, subnet_obj_check = validate_ip_and_subnet(ip_to_check, subnet_to_check)

if is_ip and is_subnet:
    if ip_obj_check in subnet_obj_check:
        print(f"IP '{ip_to_check}' is within subnet '{subnet_to_check}'.")
    else:
        print(f"IP '{ip_to_check}' is NOT within subnet '{subnet_to_check}'.")

ip_outside_subnet = "192.168.2.10"
if is_ip and is_subnet: # Re-using the valid subnet object from above
    ip_obj_outside = ipaddress.ip_address(ip_outside_subnet)
    if ip_obj_outside in subnet_obj_check:
        print(f"IP '{ip_outside_subnet}' is within subnet '{subnet_to_check}'.")
    else:
        print(f"IP '{ip_outside_subnet}' is NOT within subnet '{subnet_to_check}'.")