#!/bin/bash

# query GUDMAP/RBK for study RID
echo "curl --location --request GET 'https://www.gudmap.org/ermrest/catalog/2/entity/RNASeq:Replicate/Study_RID="${1}"'" | bash > $1_studyRID.json

# extract replicate RIDs
module load python/3.6.4-anaconda
python3 ./workflow/scripts/splitStudy.py -s $1

# run pipeline on replicate RIDs in parallel
module load nextflow/20.01.0
module load singularity/3.5.3
while read repRID; do echo ${repRID}; sleep 10; done < "$1_studyRID.csv" | xargs -P 25 -I {} nextflow run workflow/rna-seq.nf --repRID {}

# cleanup study RID files
rm $1_studyRID.json
rm $1_studyRID.csv
