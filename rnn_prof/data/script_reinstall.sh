cd ../..
python setup.py install
cd rnn_prof/data
rnn_prof irt assistments skill_builder_data_corrected_big.txt --onepo --drop-duplicates --no-remove-skill-nans --num-folds 5 --item-id-col problem_id --concept-id-col single
