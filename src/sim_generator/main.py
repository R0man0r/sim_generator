from sim_generator.models.sim_generator import SimGenerator
from sim_generator.utils.csv_utils import *
import sys

def generate_sims(count: int):
    last_id = get_last_id()
    generator = SimGenerator(last_id)

    for _ in range(count):
        sim = generator.generate()
        append_sim(sim)

def main():
    if len(sys.argv) < 2:
        print("Usage: simgen <count>")
        return

    count = int(sys.argv[1])
    generate_sims(count)
    print("Generated SIMs to src/sim_generator/db/user_db.csv")


# print("Enter a number of SIMs to generate:")
# simCount = int(input())

# generate_sims(simCount)
# print("Generated SIMs to src/sim_generator/db/user_db.csv")