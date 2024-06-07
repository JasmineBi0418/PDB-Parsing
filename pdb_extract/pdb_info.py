# Copyright (C) 2023, Jasmine Bi (bi@mirimus.com)

import pymol
from Bio.PDB import *
import warnings
class info:
    def __init__(self,pdb):
        self.pdb = pdb
    #@staticmethod
    def basic_info(self):
        PDB_data = {}       
        #pymol.cmd.load(self.pdb)
        obj = self.pdb.replace(".pdb","")
        try:
            pymol.cmd.fetch(obj,type= "pdb", async_= 0)
            chains = pymol.cmd.get_chains(obj)
            sequence = pymol.cmd.get_fastastr(obj)
        except:
            return      
        else:
            parser = PDBParser(QUIET=True)
            structure = parser.get_structure(id=obj,file=self.pdb)
            resolution = structure.header["resolution"]
            keywords = structure.header["keywords"]
            head = structure.header["head"]
            name = structure.header['name']
            structure_method = structure.header['structure_method']
            PDB_data["Name"]= name
            PDB_data["Classification"] = head
            PDB_data["Key words"] = keywords
            PDB_data["Resolution"] = resolution
            PDB_data["Structure method"] = structure_method
            PDB_data["Chains"] = chains
            PDB_data["Fasta"] = sequence
            
            return PDB_data