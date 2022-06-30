# FASTQFilter
# Language: Python
# Input: TXT
# Output: FASTQ
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin that takes a FASTQ file and filters out
sequences present in an alignment (SAM) file.

This is useful when for example removing host data
from a sample.

The plugin accepts as input a TXT file of keyword-value pairs,
tab-delimited:

fastqfile: Input FASTQ file
samfile: Input SAM filter

Output will be sent to the user-specified FASTQ.
