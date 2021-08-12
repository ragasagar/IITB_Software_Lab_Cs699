pattern=`paste -d "|" -s $1`
grep -rnE $pattern $2 |  sort -t ':'  -k1,1 -k2,2n | awk -F : '{print "path: " $1 " line no.: " $2 " line: " $3}' > output.txt