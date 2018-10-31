import yaml
import os
import subprocess
import zipfile
import tempfile
import hashlib

class Challenge:
    name = ""
    type = ""
    value = 100
    description = ""
    flag = ""
    image = False
    path = ""

    def __init__(self):
        pass
    
    def load(self, p):
        if not os.path.isdir(p):
            raise Exception("Path not exists.")
        yaml_file = os.path.join(p, "challenge.yaml")
        if not os.path.isfile(yaml_file):
            raise Exception("challenge.yaml not exists.")
        with open(yaml_file) as f:
            data = yaml.load(f)
        self.name = data["name"]
        self.type = data["type"]
        self.value = data["value"]
        self.description = data["description"]
        self.flag = data["flag"]
        self.image = data["image"]
        self.short_name = os.path.basename(p).lower()
        self.path = p

    def build_image(self, registry=None):
        if not self.image:
            return
        image_name = self.short_name
        if registry:
            image_name = "%s/%s" %(registry, self.short_name)
        subprocess.check_call(["docker", "build", "-t", image_name, self.path])
        
    
    def pack_zip(self, dist):
        dist_src = os.path.join(self.path, "dist")
        if not os.path.isdir(dist_src):
            return
        filelist = []
        for i in os.listdir(dist_src):
            if i.startswith("."):
                continue
            filelist.append((os.path.join(dist_src, i), i))
        if len(filelist) == 0:
            return None
        with tempfile.TemporaryFile() as tmpf:
            with zipfile.ZipFile(tmpf, mode="w", compression=zipfile.ZIP_DEFLATED) as zipf:
                for ft in filelist:
                    zipf.write(ft[0], ft[1])
            tmpf.seek(0)
            sha256 = hashlib.sha256()
            sha256.update(tmpf.read())
            digest = sha256.hexdigest()
            fname = "%s_%s.zip" % (self.short_name, digest)
            fpath = os.path.join(dist, fname)
            tmpf.seek(0)
            with open(fpath, "w+b") as f:
                f.write(tmpf.read())
        return fname

    def get_ctfd_portable(self):
        ret = {}
        ret["name"] = self.name
        ret["category"] = self.type
        ret["flags"] = [{"flag": self.flag}]
        ret["description"] = self.description
        ret["value"] = self.value
        return ret
            
