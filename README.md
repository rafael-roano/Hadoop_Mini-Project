# Hadoop Mini Project - Automobile Post-sales Report Report

This is a basic MapReduce program that assists an automobile tracking platform to generate a report of one of their business key metrics.

## Description

The platform tracks the history of incidents after the initital sale of new vehicles. Incidents tracked include subsequent private sales, repairs, and accidents. The platform provides a references for second-hand buyers to understand the vehicles they are interested in.

The MapReduce operation produces a report of the total number of accidents per make and year of the car.

MapReduce operation consists of:

1. Map Task 1: Read history reports and generate intermediate key-value pairs (vin_number, [incident type, make, year])

2. Sort: Output of the mapper is sorted based on key-value pairs

3. Reduce Task 1: Read sorted key-value pairs, filter and propagate make and year to the accident records

4. Map Task 2: Read reduced output and generate composite keys constructed by vehicle make and year. Value is the count of 1

5. Sort: Output of the mapper is sorted based on key-value pair

6. Reducer Task 2: Read sorted key-value pairs and count the individual values by key. The output key is the combination of make and year. Value is the count

## Getting Started

### Dependencies

* [Hortonworks Hadoop Sandbox][1] (HDP_3.0.1_virtualbox_181205)
* Python 2.7 (included in HDP)
* hadoop-streaming.jar (included in HDP)
* Windows 10

[1]: https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html

### Installing

**Hadoop Setup**

Using Hortonworks Hadoop Sandbox is recommended. This sandbox is a pre-configured virtual machine that has all necessary installation completed. Installation steps can be found [here][2]

[2]: https://www.youtube.com/watch?v=735yx2Eak48

**Files**

1. Download Data source and Python scripts from https://github.com/rafael-roano/Hadoop_Mini-Project.git. These are:
    * data.csv
    * autoinc_mapper1.py
    * autoinc_reducer1.py
    * autoinc_mapper2.py
    * autoinc_reducer2.py

2. Save data.csv file in a HDFS location
3. Save mappers and reducers scripts in local file (within the sandbox environment)


# TBD:

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Rafael Roano

## Version History

* 0.1
    * Initial Release