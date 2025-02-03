#!/usr/bin/env python

from Bio import SeqIO

TARGET_LENGTH_SUM = 2E7

cds_file = "Ahypochondriacus_315_v1.0.cds_primaryTranscriptOnly.fa"
with open(cds_file, 'r') as fin:
    cds_records = list(SeqIO.parse(fin, format='fasta'))
    print(f"Number of CDS sequences: {len(cds_records)}")

cds_record_lengths = [len(rec.seq) for rec in cds_records]
original_length_sum = sum(cds_record_lengths)
print(f"Original total CDS bp: {original_length_sum}")

ratio  = TARGET_LENGTH_SUM / original_length_sum
print(f"Ratio of sequences to keep on 5' ends: {ratio}")

for rec in cds_records:
    rec.seq = rec.seq[:int(len(rec.seq) * ratio)]

cds_record_lengths = [len(rec.seq) for rec in cds_records]
new_length_sum = sum(cds_record_lengths)

print(f"New total CDS bp: {new_length_sum}")

outfile = "Ahypochondriacus_315_v1.0.cds_primaryTranscriptOnly.cter_trimmed.fa"
print(f"Writing {len(cds_records)} sequences to {outfile}")
SeqIO.write(cds_records, outfile, "fasta")

print("Done")


