# Copyright (C) 2023, Jasmine Bi (bi@mirimus.com)
import pymol
class rmsd:
    def __init__(self,subject,query):
        self.subject = subject
        self.query = query
    #@staticmethod
    def general_align(self):
        """Do alignment between two pdbs and return rmsd.
        ----------
        Parameters
        subject : A PDB file. Sequence will be first in the alignment.
        query : A PDB file. Sequence will be second in alignment.
        cycle = 0: no outlier rejection
        transform = 0 : do not superimpose
        return: rmsd
        ----------
        """
        pymol.finish_launching()
        pymol.cmd.load(self.subject)
        pymol.cmd.load(self.query)
        obj = list(pymol.cmd.get_object_list('all'))
        #file_name = str(filename) + ".aln"
        if len(obj)!=2:
            general_rmsd = "NA"
            print("at least one of the file is empty!")
        else:
            results = pymol.cmd.align(obj[0], obj[1],object='aln', cycles = 0, transform=0)
            general_rmsd = results[0]
            #pymol.cmd.save(file_name, 'aln')
        pymol.cmd.reinitialize()
        #time.sleep(1)
        print("general alignment of {} and {}".format(self.subject,self.query))
        return general_rmsd
    #@staticmethod
    def super_align(self):
        """Do alignment between two pdbs and calculate superposition rmsd.
        ----------
        Parameters
        subject : A PDB file. Sequence will be first in the alignment.
        query : A PDB file. Sequence will be second in alignment.
        cycle = 0: no outlier rejection
        transform = 1 : do superposition
        return : superposition rmsd
        ----------
        """
        pymol.finish_launching()
        pymol.cmd.load(self.subject)
        pymol.cmd.load(self.query)
        obj = list(pymol.cmd.get_object_list('all'))
        #file_name = str(filename) + ".aln"
        if len(obj)!=2:
            super_rmsd = "NA"
            print("at least one of the file is empty!")
        else:
            results = pymol.cmd.super(obj[0], obj[1], object='aln', cycles = 0, transform=1)
            super_rmsd = results[0]
            #pymol.cmd.save(file_name, 'aln')
        pymol.cmd.reinitialize()
        #time.sleep(1)
        print("superposition alignment of {} and {}".format(self.subject,self.query))
        return super_rmsd
    #@staticmethod
    def ce_align(self):
        """Do alignment using the CE algorithm and return cealign rmsd.
        ----------
        Parameters
        subject : A PDB file. Sequence will be first in the alignment.
        query : A PDB file. Sequence will be second in alignment.
        transform = 0 : do not do superposition
        window = 3 : will have errors if the target/mobile length is shorter than 2*window.
        return : rmsd and alignment_length
        ----------
        """
        pymol.finish_launching()
        pymol.cmd.load(self.subject)
        pymol.cmd.load(self.query)
        obj = list(pymol.cmd.get_object_list('all'))
        #file_name = str(filename) + ".aln"
        if len(obj)!=2:
            ce_rmsd = "NA"
            print("at least one of the file is empty!")
        else:
            results = pymol.cmd.cealign(obj[0], obj[1],window=3,transform= 1)
            ce_rmsd= results['RMSD']
            alignment_length = results['alignment_length']
            #pymol.cmd.save(file_name, 'aln')
        pymol.cmd.reinitialize()
        #time.sleep(1)
        #print(align_detail)
        print("CE alignment of {} and {}".format(self.subject,self.query))
        return ce_rmsd