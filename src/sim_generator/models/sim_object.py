from dataclasses import dataclass

@dataclass
class SimObject:
    id: int
    name: str
    auth: str
    imsi: str
    key: str
    op_type: str
    opc: str
    amf: str
    sqn: str
    qci: str
    ip_alloc: str
    iccid: str