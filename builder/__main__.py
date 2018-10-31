from .challenge import Challenge
import sys
from os import path
import os
import yaml

def main():
    if len(sys.argv) < 2:
        return
    # TODO: change to argparser
    challenges = []
    chal_path = sys.argv[1]
    os.makedirs("dists/uploads", exist_ok=True)
    for d in os.listdir(chal_path):
        rp = path.join(chal_path, d)
        if not path.isdir(rp):
            continue
        chal = Challenge()
        chal.load(rp)
        print(chal.name)
        challenges.append(chal)
    portable = []
    for chal in challenges:
        chal.build_image()
        chal_data = chal.get_ctfd_portable()
        print(chal_data)
        zip_file = chal.pack_zip("dists/uploads/")
        if zip_file:
            chal_data["files"] = [zip_file]
        portable.append(chal_data)
    with open("dists/challenges.yaml", "w+") as f:
        yaml.dump(portable, stream=f)
    

        



if __name__ == "__main__":
    main()