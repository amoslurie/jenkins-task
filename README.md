# jenkins-task
This is a Python script for a jenkins task.
Prints an argument based sequence parameter.
The number of arguments should be 2

## manual usage 
```
python script.py <argument> <sequence>
```

## invoke by jenkins

step #1
`jenkins job 01-checkout-job`
```
Checkput source from gt to hared workspace.
Saves environment varibles to a file: "hudsonBuild.properties"
If completed with stable state, triggers step #2.
```
step #2
`jenkins job 02-execute-sacript`
```
Execute the python script with the job name and build number as parameters.
Retries 3 times until sucssed and triggers step #3.
```
step #3
`jenkins job 03-print-build-number`
```
Prints the build number of step #1 from the environment variabale file
```

