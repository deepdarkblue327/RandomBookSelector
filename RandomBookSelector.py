class RandomBookSelector:
    
    types = {"epub":[],"pdf":[],"mobi":[],"others":[],"bad_ext":[]}
    
    def __init__(self,path=""):
        import sys,os,random
        for r,d,file in os.walk(path):
            for f in file:
                if ".epub" in f.lower():
                    self.types["epub"].append(f)
                elif ".mobi" in f.lower():
                    self.types["mobi"].append(f)
                elif ".pdf" in f.lower():
                    self.types["pdf"].append(f)
                else:
                    self.types["others"].append(f)
                    self.types["bad_ext"].append(f.strip().split(".")[-1])
        self.types["bad_ext"] = list(set(self.types["bad_ext"]))
    
    def ext(self,string=""):
        return string.strip().split(".")[-1]
    
    def find_random(self,file_format="",exclude=False):
        if exclude == False:
            return self.types[file_format][random.randint(0,len(self.types[file_format]))]
        else:
            #exclude_files = [j for i in self.types.keys() for j in self.types[i] if i not in file_format and self.ext(j) not in self.types["ext"]]
            exclude_files = []
            for i in self.types.keys():
                if i not in file_format:
                    for j in self.types[i]:
                        if self.ext(j) not in self.types["bad_ext"]:
                            exclude_files.append(j)
            return exclude_files[random.randint(0,len(exclude_files))] if len(exclude_files) != 0 else None

