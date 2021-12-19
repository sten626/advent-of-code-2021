import fileinput
from bitstring import BitArray, BitStream


class Packets:
    op_literal = 4

    def __init__(self, bitstream) -> None:
        self._bitstream = bitstream

    def _get_header(self):
        version = self._bitstream.read("uint:3")
        type_id = self._bitstream.read("uint:3")
        return version, type_id

    def _get_literal(self):
        result = BitArray()

        while True:
            bits = self._bitstream.read(5)
            lead = bits.read(1)
            rest = bits.read(4)
            result.append(rest)

            if lead.startswith("0b0"):
                break

        return result.uint

    def next(self):
        version, type_id = self._get_header()

        if type_id == Packets.op_literal:
            literal = self._get_literal()


def parse_file():
    return next(fileinput.input()).strip()


hex_input = parse_file()
stream = BitStream("0x" + hex_input)
packets = Packets(stream)
packets.next()
# bits = bin(int(hexi, 16))[2:]
# version = int(bits[0:3], 2)
# print(version)
# type_id = int(bits[3:6], 2)
# print(type_id)
# i = 6
# value = ""

# while True:
#     chunk = bits[i : i + 5]
#     print(chunk)
#     value += chunk[1:]

#     if chunk[0] == "0":
#         break

#     i += 5

# value = int(value, 2)
# print(value)
