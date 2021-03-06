#!/usr/bin/env python
from __future__ import division

__author__ = "Giorgio Casaburi and Greg Caporaso"
__copyright__ = "Copyright 2013, The meta-miRNA project"
__credits__ = "Giorgio Casaburi", "Greg Caporaso"
__license__ = "GPL"
__version__ = "0.0.0-dev"
__maintainer__ = "Giorgio Casaburi"
__email__ = "casaburi@ceinge.unina.it"

from pyqi.core.command import Command, Parameter, ParameterCollection

class SraToQiime(Command):
    BriefDescription = "post split libraries format: This script allows to convert .sra miRNA sequence data into a QIIME compatible format"
    LongDescription = "A script for converting SRA miRNA sequence data into a format that can be used with QIIME's closed reference OTU picking workflows. THIS CODE IS CURRENTLY UNTESTED. YOU SHOULD NOT USE THIS VERSION OF THE CODE. THIS MESSAGE WILL BE REMOVED WHEN TESTS ARE ADDED."
    Parameters = ParameterCollection([
        Parameter(Name='input_sra', DataType=str,
                  Description='your input .sra file', Required=True),
        Parameter(Name='output_dir', DataType=str,
                  Description='the output directory', Required=True,
                  Default=True)
    ])

# sratoolkit and SCHIRMP are required to be installed by the User so that the tools sra_dumo and fastq_to_fasta can be called in the command line within the User $HOME.

sra_dump_path = "$PATH/fastq-dump.2.3.1"
fastq_to_fasta = "$PATH/fastq_to_fasta"

    def run(self, **kwargs):
        
    
    
    input_filepaths = Kwargs['input_sra']
    
    create_dir = Kwargs['output_dir']
    
    output_dir = Kwargs['output_dir']


    for input_filepath in input_filepaths:
        output_filepath = join(output_dir, input_filepath + ".fastq")
      command = "%s %s -O %s" % (sra_dump_path, input_filepath, output_filepath)

     stdout, stderr, ret_val = pyqi_system_call(command)
     command = "rm %s" % (input_filepath)

     stdout, stderr, ret_val = pyqi_system_call(command)

     command = "%s %s/*.fastq > %s.fast" % (fastq_to_fasta, output_filepath, output_filepath)

     stdout, stderr, ret_val = pyqi_system_call(command)
     command = "rm %s/*.fastq" % (output_filepath)

     stdout, stderr, ret_val = pyqi_system_call(command)
     command = "sed 's/\./_/g;s/ .*$//g' %s*.fast > %s.fasta" % (output_filepath, output_filepath)

     stdout, stderr, ret_val = pyqi_system_call(command)
        command = "rm %s*.fast" % (input_filepath)

     stdout, stderr, ret_val = pyqi_system_call(command)
    

CommandConstructor = sra_to_qiime




