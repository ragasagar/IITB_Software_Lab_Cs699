pattern=`paste -d "|" -s $1`
grep -r -n  -E $pattern $2 |  sort  -k1,1 -k2,2n -t  ':'| awk -F : '{print "path: " $1 " line no.: " $2 " line: " $3}' > output.txt