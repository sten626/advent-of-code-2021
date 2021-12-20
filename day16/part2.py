import fileinput
from bitstring import BitArray, BitStream
from math import prod


class Packets:
    op_sum = 0
    op_prod = 1
    op_min = 2
    op_max = 3
    op_literal = 4
    op_gt = 5
    op_lt = 6
    op_eq = 7

    def __init__(self, bitstream) -> None:
        self._bitstream = bitstream

    def _get_header(self):
        version = self._bitstream.read("uint:3")
        type_id = self._bitstream.read("uint:3")
        return version, type_id

    def _get_literal(self):
        result = BitArray()
        bit_length = 0

        while True:
            bits = self._bitstream.read(5)
            bit_length += 5
            lead = bits.read(1)
            rest = bits.read(4)
            result.append(rest)

            if lead == "0b0":
                break

        return result.uint, bit_length

    def _get_subpackets(self):
        subpackets = []
        length_type_id = self._bitstream.read(1)
        bit_length = 1

        if length_type_id == "0b0":
            subpacket_lengths = self._bitstream.read(15).uint
            bit_length += 15

            while subpacket_lengths > 0:
                packet, packet_bit_length = self._next()
                subpackets.append(packet)
                bit_length += packet_bit_length
                subpacket_lengths -= packet_bit_length
        else:
            n_subpackets = self._bitstream.read(11).uint
            bit_length += 11

            while n_subpackets > 0:
                packet, packet_bit_length = self._next()
                subpackets.append(packet)
                bit_length += packet_bit_length
                n_subpackets -= 1

        return subpackets, bit_length

    def _next(self):
        version, type_id = self._get_header()

        if type_id == Packets.op_literal:
            literal, bit_length = self._get_literal()
            return (version, type_id, literal), bit_length + 6
        else:
            subpackets, bit_length = self._get_subpackets()
            return (version, type_id, subpackets), bit_length + 6

    def result(self):
        def _result(packet):
            (_, type_id, value) = packet

            if type_id == Packets.op_literal:
                return value

            subpacket_results = (_result(packet) for packet in value)

            if type_id == Packets.op_sum:
                return sum(subpacket_results)
            if type_id == Packets.op_prod:
                return prod(subpacket_results)
            if type_id == Packets.op_min:
                return min(subpacket_results)
            if type_id == Packets.op_max:
                return max(subpacket_results)

            first = next(subpacket_results)
            second = next(subpacket_results)

            if type_id == Packets.op_gt:
                return 1 if first > second else 0
            if type_id == Packets.op_lt:
                return 1 if first < second else 0
            if type_id == Packets.op_eq:
                return 1 if first == second else 0

            raise RuntimeError("Unknown type_id {}".format(type_id))

        packet, _ = self._next()
        return _result(packet)


def parse_file():
    return next(fileinput.input()).strip()


def version_sum(root_packet):
    version, type_id, subp = root_packet

    if type_id == Packets.op_literal:
        return version

    return version + sum(version_sum(p) for p in subp)


hex_input = parse_file()
stream = BitStream("0x" + hex_input)
packets = Packets(stream)
print(packets.result())
