from models.sim_generator import SimGenerator
from utils.csv_utils import *

def generate_sims(count: int):
    last_id = get_last_id()
    generator = SimGenerator(last_id)

    for _ in range(count):
        sim = generator.generate()
        append_sim(sim)

print("Enter a number of SIMs to generate:")
simCount = int(input())

generate_sims(simCount)
print("Done.")