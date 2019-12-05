# vo2app
This is a command line tool that can be used to get relative percentiles for individuals based on sex, age, and vo2 max scores.
The percentiles are based on equations gathered from the following sources: 
- [KUMC](http://www.kumc.edu/fitness-ranking.html)
- [shiny-data](https://vo2peak.shinyapps.io/vo2peak_calculator/)

## Setup
Clone repo:
- `git clone https://github.com/zkhan12/vo2app.git`

Enter repo:
- `cd vo2app`

Install tool:
- `pip install .`

### Update
The tool will need to be reinstalled whenever a a pull is made from the repo, to update run `git pull origin master` followed by `pip install .`
## How to use
Run the command below, note `outputfile` and `datasource` are optional parameters, for more info run `voconv -h`

By default all output files will be stored in the output folder unless a specified location is given
`voconv <inputfile> <outputfile> <datasource>`
