#!/bin/bash

if [ $1 == "--help" ] || [ $1 == "-h" ] || [ $# != "3" ]
then
    if [ $# != "3" ]
    then
        echo "[ERROR] You provided $# arguments"
    fi
    echo "USAGE: script.sh <input-folder-name> <output-folder-appendix> <mode>"
    echo "       <input-folder-name> must NOT contain the '/'"
    echo "       <mode> must be either irt or hirt"
    echo "       The output folder is created as 'output-'+<input-folder-name>+-+<output-folder-appendix>"
else

    in_folder=$1
    out_appendix=$2
    mode=$3
    out_folder="output-"$in_folder"-"$out_appendix"/"

    echo "[INFO] Input folder name: $1"
    echo "[INFO] Folder Appendix: $2"
    echo "[INFO] Output Folder Name: $out_folder"
    echo "[INFO] Mode $3"

    mkdir $out_folder
    cd $in_folder

    for filename in ./*; do
        cp $filename ../
        echo "[INFO] Working on $filename"
        cd ..
        python split_data.py $filename "Anon Student Id" "\t"
        shortened_name="${filename:0:-4}"
        echo "[INFO] shortened name: $shortened_name"
        if [ "$mode" == "irt" ]
        then
            rnn_prof irt kddcup $shortened_name"_big.txt" --onepo --drop-duplicates --no-remove-skill-nans --num-folds 5 --item-id-col 'Step Name' --concept-id-col single &> $shortened_name"-output-estimation"
        else
            if [ "$mode" == "hirt" ]
            then
                rnn_prof irt kddcup $shortened_name"_big.txt" --onepo --drop-duplicates --no-remove-skill-nans --num-folds 5 --item-precision 2.0 --template-precision 4.0 -m 5000 --template-id-col 'Problem Name' --item-id-col 'Step Name' --concept-id-col single &> $shortened_name"-output-estimation"
            else
                echo "[ERROR] no correct mode was specified"
            fi
        fi
        mv $shortened_name"-output-estimation" $out_folder
        rm $filename
        rm $shortened_name"_big.txt"
        rm $shortened_name"_small.txt"
        cd $in_folder
done
fi
