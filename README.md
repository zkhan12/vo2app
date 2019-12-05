# vo2app
This is a command line tool that can be used to get relative percentiles for individuals based on sex, age, and vo2 max scores.
The percentiles are based on equations gathered from the following sources: 
- [KUMC](http://www.kumc.edu/fitness-ranking.html)
- [Saarland University](https://vo2peak.shinyapps.io/vo2peak_calculator/)

## Setup
Clone repo:
- `git clone https://github.com/zkhan12/vo2app.git`

Enter repo:
- `cd vo2app`

Install tool:
- `pip install .`

#### Update
The tool will need to be reinstalled whenever a a pull is made from the repo, to update run `git pull origin master` followed by `pip install .`

## How to use
Run the command below to get percentile outputs, note `outputfile` and `datasource` are optional parameters, for more info run `voconv -h`

`voconv <inputfile> <outputfile> <datasource>`

By default all output files will be stored in the output folder (`cd output`) unless a specified location is given. The default data source is KUMC.

#### Input structure
The inputfile must be a csv. If the input file contains a header, it must have sex, age, and vo2 columns, in any order. If it contains no header, the order is assumed to be sex, age, and vo2, in that order. For the sex column, all values must be either [m, Male, MALE, M] or [f, Female, FEMALE, F]. Other values in the sex column will not be processed. Below is a possible sample format for the input file.

Sample.csv
```
sex,age,vo2
m,22,35
m,45,35
f,21,30
m,44,38
```
