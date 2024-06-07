# Copyright (C) 2023, Jasmine Bi (bi@mirimus.com)
import pymol
import pdb_info
class extract:
    def __init__(self,pdb,chain,seq):
        self.pdb = pdb
        self.chain = chain
        self.seq = seq
        #print("Extracted {}, chain {}, and residues {} ".format(self.pdb,self.chain,self.seq))
    #@staticmethod
    def extract_chain(self):
        """ 
        extract Chain from a pdb file and save PDB chain file
        -------
        Parameters
        pdb: pdb file 
        chain: chain name, make sure your pdb file has the input chain name
        -------
        """
        pymol.finish_launching()
        pymol.cmd.load(self.pdb)
        pdb_data = pdb_info.info(self.pdb).basic_info()
        all_chains =pdb_data['Chains'] 
        if self.chain in all_chains:
            chain_arg ="chain " + self.chain
            obj = self.pdb.replace(".pdb","")
            chain_name = obj + "_" + self.chain
            filename =  chain_name + ".pdb"
            pymol.cmd.extract(str(chain_name), str(chain_arg))
            pymol.cmd.delete(str(obj))
            pymol.cmd.save(filename)
            pymol.cmd.reinitialize()
            print("--->{} file saved in your current working dir!".format(filename))

        else:
            filename="NA"
            print("Error: chain {} not found in {}".format(self.chain,self.pdb))
            print("{} has chains: {}".format(self.pdb,all_chains))    
        return filename
    # @staticmethod
    def extract_pep(self):
        """ 
        extract structure according to kmer residues
        and save substructure of input PDB file
        ---------
        Parameters
        pdb: pdb files
        chain: chain name
        seq: residue sequence
        ----------
        """
        obj = self.pdb.replace(".pdb","")
        chain_name = obj + "_" + self.chain
        filename =  extract.extract_chain(self)
        obj2 = filename.replace(".pdb","") 
        if filename!='NA':
            pymol.finish_launching()
            pymol.cmd.load(filename)
            sequence_arg ="pepseq " + self.seq
            pymol.cmd.extract("peptide", str(sequence_arg))
            obj_chain =  filename.replace(".pdb","")
            pymol.cmd.delete(str(obj_chain))
            filename_pep = chain_name + "_"+ self.seq + ".pdb" 
            pymol.cmd.save(filename_pep)
            pymol.cmd.reinitialize()
            print("--->{} file saved in your current working dir!".format(filename_pep))
        else:
            return False
        return filename_pep