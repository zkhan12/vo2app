# vo2app
This is a command line tool that can be used to get relative percentiles for individuals based on sex, age, and relative vo2 max scores.
The percentiles are based on equations gathered from the following sources: 
- [University of Kansas Medical Center](http://www.kumc.edu/fitness-ranking.html)
- [Saarland University](https://vo2peak.shinyapps.io/vo2peak_calculator/)
  - Note: su sources only support age ranges of 22-75 and relative vo2 max scores between 11-61

# Setup

### Option 1
Install tool:
- `pip install git+https://github.com/zkhan12/vo2app.git`

### Option 2
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

By default all output files will be stored in the directory where voconv is called unless a specified location is given. The default data source is KUMC.

#### Input structure
The inputfile must be a csv. If the input file contains a header, it must have sex, age, and vo2 columns, in any order. If it contains no header, the order is assumed to be sex, age, and vo2, in that order. For the sex column, all values must be either [m, Male, MALE, M] or [f, Female, FEMALE, F]. Other values in the sex column will not be processed. Below is a possible sample format for the input file.

Sample.csv
```
sex,age,vo2
m,22,35.1
m,45,35.72
f,25,30.3
m,44,38.05
```
