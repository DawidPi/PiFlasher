import sys
import os.path
import serial
import usb

class PiFlasher:
    def __init__(self):
        pass


def hex_file_provided():
    num_arguments = len(sys.argv)
    if num_arguments < 2:
        print("File to flash was not given.")
        return False
    if num_arguments > 2:
        print("Too many arguments given.")
        return False

    extensions = os.path.splitext(sys.argv[1])
    no_hex_extension_error = "Given file does not have 'hex' extension."

    if len(extensions) < 1:
        print(no_hex_extension_error)
        return False

    if extensions[1] != ".hex":
        print(no_hex_extension_error)
        return False

    return True


if __name__ == "__main__":
    if not hex_file_provided():
        print("\nAborting\n")
        sys.exit(1)

    devices = usb.core.find(find_all=True)
    for device in devices:
        print(device)