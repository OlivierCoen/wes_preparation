# Prepare BED file for Whole Exome sequencing

## Step 1: Download data from Phytozome

Download all files from https://data.jgi.doe.gov/refine-download/phytozome?q=Amaranthus+hypochondriacus
Unzip the file in the root folder of this repo (the resulting folder should be named Phytozome)


## Step 2: Install and run Interproscan (Optional)

Install interproscan locally and run it with the following command:
```bash    
./interproscan.sh \
    --input Ahypochondriacus_315_v1.0.protein.fa \
    --cpu 6
```
You can skip this step but you'll need to adapt the parse_iprscan_results.ipynb notebook to parse the file:
Phytozome/PhytozomeV12/Ahypochondriacus/annotation/Ahypochondriacus_315_v1.0.description.txt
instead of the interproscan output


## Step 3: Create environment

Requirements are contained in conda-linux-64.lock:

```bash
micromamba env create -f conda-linux-64.lock -n wes
micromamba activate wes
```

## Step 4: Get list of unwated proteins

Launch jupyter
```bash     
jupyter notebook
```

And run the notebook:
```bash  
parse_iprscan_results.ipynb
```
to create the file unwanted_proteins.txt


## Step 5: Trim CDS sequences in the GFF3 file

Run the notebook:
```bash 
trim_cds_sequences_in_gff.ipynb
```
to create the new GFF3 file containing the trimmed CDS Ahypochondriacus_315_v1.0.gene.cds_only.cter_trimmed.gff3

## Step 6: Check this new GFF3 file

Run AGAT to create a clean FASTA file:
```bash 
agat_sp_extract_sequences.pl \
  --gff Ahypochondriacus_315_v1.0.gene.cds_only.cter_trimmed.gff3 \
  --fasta Phytozome/PhytozomeV12/Ahypochondriacus/assembly/Ahypochondriacus_315_v1.0.fa \
  -o Ahypochondriacus_315_v1.0.gene.cds_only.cter_trimmed.fa
```

And now run the notebook:
```bash
check_new_cds_sequences.ipynb
```
You should see no error!

## Step 7: Create BED file from the GFF3

```bash
agat_convert_sp_gff2bed.pl \
  --gff Ahypochondriacus_315_v1.0.gene.cds_only.cter_trimmed.gff3 \
  -o Ahypochondriacus_315_v1.0.gene.cter_trimmed.bed
```

## Step 8: Check BED file

```bash
bedtools getfasta \
  -fi Phytozome/PhytozomeV12/Ahypochondriacus/assembly/Ahypochondriacus_315_v1.0.fa \
  -bed Ahypochondriacus_315_v1.0.gene.cter_trimmed.bed \
  -fo Ahypochondriacus_315_v1.0.gene.cter_trimmed.from_bed.fa \
  -name -s -split
```

And now run the notebook:
```bash
check_new_cds_sequences_from_bed.ipynb
```
You should see no error!
