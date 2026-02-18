import csv
import os
from pathlib import Path
from models.sim_object import SimObject

DB_FILE = Path("src/sim_generator/db/user_db.csv")

def get_last_id() -> int:
    if not DB_FILE.exists():
        return 0

    with DB_FILE.open(newline="") as f:
        reader = list(csv.reader(f))

        if len(reader) <= 1:
            return 0

        return int(reader[-1][0])
    
def append_sim(sim: SimObject):
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)

    file_exists = DB_FILE.exists()

    with DB_FILE.open("a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "ID","Name","Auth","IMSI","Key",
                "OP_Type","OP/OPc","AMF",
                "SQN","QCI","IP_alloc","ICCID"
            ])

        writer.writerow([
            sim.id, sim.name, sim.auth, sim.imsi,
            sim.key, sim.op_type, sim.opc,
            sim.amf, sim.sqn, sim.qci,
            sim.ip_alloc, sim.iccid
        ])