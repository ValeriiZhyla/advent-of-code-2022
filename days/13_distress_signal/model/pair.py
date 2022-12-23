from .packet import Packet

class PacketPair:
    fst: Packet = None
    snd: Packet = None

    def __init__(self, first: Packet, second: Packet):
        self.fst = first
        self.snd = second
