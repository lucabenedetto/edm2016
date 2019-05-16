#!/bin/bash
folder_name="by_skill-20190516-1015-kdd/"
mkdir 'output'-$folder_name
cd $folder_name
for filename in ./*; do
    cp $filename ../
    echo $filename
    cd ..
    python split_data.py $filename "Anon Student Id" "\t"
    # HIRT
    # rnn_prof irt kddcup _big.txt --onepo --drop-duplicates --no-remove-skill-nans --num-folds 5 --item-precision 2.0 --template-precision 4.0 -m 5000 --template-id-col template_id --item-id-col problem_id --concept-id-col single &> $filename"-output-estimation"
    # IRT
    rnn_prof irt kddcup _big.txt --onepo --drop-duplicates --no-remove-skill-nans --num-folds 5 --item-id-col 'Step Name' --concept-id-col single &> $filename"-output-estimation"
    mv $filename"-output-estimation" "output-"$folder_name
    rm $filename
    cd $folder_name
done
cd ..
rm _big.txt
rm _small.txt
