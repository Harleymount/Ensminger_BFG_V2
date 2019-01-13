import argparse
import logging
import logging.config
import os
import glob
import re
import param
import create_fasta
import alignment
import supplements
import read_counts
import plot

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='BFG-Y2H')
    
    # make fasta from summary file (AD and DB)
    # -- create: creates fasta file from summary.csv
    # -- build: if the fasta files already exist, build index files for them
    parser.add_argument('--pfasta', help="Path to fasta file")
#    parser.add_argument("--adgroup", help="AD group number", required=True)
#    parser.add_argument("--dbgroup", help="DB group number", required=True)

    # parameters for cluster
    parser.add_argument("--fastq", help="Path to all fastq files you want to analyze")
    parser.add_argument("--output", help="Output path for sam files")
    
    # for analysis
    parser.add_argument("--r1", help=".sam file for read one")
    parser.add_argument("--r2", help=".sam file for read two")

    args = parser.parse_args()
    
    # required arguments
    #AD_GROUP = args.adgroup
    #DB_GROUP = args.dbgroup

    #AD_REF = REF_PATH+"y_AD_"+AD_GROUP
    #DB_REF = REF_PATH+"y_DB_"+DB_GROUP

    # processing fasta file
    fasta_output = args.pfasta
         
    if fasta_output is not None:
        # example of create fasta for AD1DB4
        create_fasta.create_fasta(AD_summary, DB_summary, fasta_output, group_spec=True, AD=AD_GROUP, DB=DB_GROUP)

        # example of create fasta for all 
#        create_fasta(AD_summary, DB_summary, fasta_output)

        list_fasta = os.listdir(fasta_output)

        for fasta in list_fasta:
            create_fasta.build_index(os.path.join(fasta_output,fasta), fasta_output)
