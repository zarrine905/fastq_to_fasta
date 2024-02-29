def fastq_to_fasta(fastq_file, fasta_file):
    with open(fastq_file,'r') as fq:
        with open(fasta_file, 'w') as fa:
            while True:
                # Read four lines at a time from the FASTQ file
                header = fq.readline().strip()
                if not header:
                    break  # end of file
                seq = fq.readline().strip()
                fq.readline()  # discard the third line (quality header)
                qual = fq.readline().strip()

                # Write to the FASTA file
                fa.write(f'>{header[1:]}\n{seq}\n')

# Usage example
fastq_file = 'input.fastq'
fasta_file = 'output.fasta'
fastq_to_fasta(fastq_file, fasta_file)
