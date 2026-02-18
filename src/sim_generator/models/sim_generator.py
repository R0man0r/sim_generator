import secrets
from sim_generator.models.sim_object import SimObject
from sim_generator.utils.iccid_generator import generate_iccid

class SimGenerator:

    def __init__(self, starting_id: int):
        self.current_id = starting_id


    def generate(self) -> SimObject:
        self.current_id += 1
        return SimObject(
            id=self.current_id,
            name=f"ue{self.current_id}",
            auth="mil",
            imsi=self.generate_imsi(),
            key=self.generate_key(),
            op_type="opc",
            opc=self.generate_opc(),
            amf="8000",
            sqn="0000000012fa",
            qci="7",
            ip_alloc="dynamic",
            iccid=generate_iccid()
        )

    def generate_imsi(self) -> str:
        return "40166" + ''.join(str(secrets.randbelow(10)) for _ in range(10))

    def generate_key(self) -> str:
        return secrets.token_hex(16)

    def generate_opc(self) -> str:
        return secrets.token_hex(16)