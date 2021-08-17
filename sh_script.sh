hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-files autoinc_mapper1.py,autoinc_reducer1.py -mapper autoinc_mapper1.py -reducer autoinc_reducer1.py \
-input data.csv -output preresults

hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
-files autoinc_mapper2.py,autoinc_reducer2.py -mapper autoinc_mapper2.py -reducer autoinc_reducer2.py \
-input preresults -output final_results