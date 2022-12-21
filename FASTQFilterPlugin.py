import sys
import PyPluMA
class FASTQFilterPlugin:
    def input(self, inputfile):
       infile = open(inputfile, 'r')
       params = dict()
       for line in infile:
           contents = line.strip().split('\t')
           params[contents[0]] = contents[1]
       self.fastqfile = open(PyPluMA.prefix()+"/"+params["fastqfile"], 'r')
       self.samfile = open(PyPluMA.prefix()+"/"+params["samfile"], 'r')

    def run(self):
       self.aligned = set()
       for line in self.samfile:
          seqname = line.strip().split('\t')[0]
          self.aligned.add(seqname)

    def output(self, outfile):
       outfastq = open(outfile, 'w')
       outfastq2 = open(outfile+".rejected.fastq", 'w')
       pos = 0
       for line in self.fastqfile:
          if (pos % 4 == 0):
              lines = []
              lines.append(line)
              seqname = line.strip().split(' ')[0]
              seqname = seqname[1:]
          elif (pos % 4 == 3):
              lines.append(line)
              if (seqname not in self.aligned):
                  for i in range(0, 4):
                      outfastq.write(lines[i])
              else:
                  for i in range(0, 4):
                      outfastq2.write(lines[i])
          else:
              lines.append(line)
          pos += 1

