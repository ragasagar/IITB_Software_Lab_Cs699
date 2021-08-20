#!bin/bash


# {
#     my_dict[$1,$4] +=$5
# }
# {

# }
# END { 
#     for (key in my_dict) 
# { 
#     print $1 ": " my_dict[key]
#      } 
#          for (key in count) 
# { 
#     print key ": " count[key]
#      } 
#      }'

awk -F"\t" '
BEGIN { SUBSEP = OFS = FS } { s[$1,$2,$3] += $4;  } END { for (i in s) { print i, s[i]} }
' $1  | awk -F"\t" '
BEGIN { 
    SUBSEP = OFS = FS 
} 
{ s[$1,$2] += $4; count[$1,$2]++;
} 
END { print"Roll_no\tName\tNum_courses\tPercentage"; 
for (i in s) { print i, count[i], s[i]/count[i]}
}
' | sort -t' ' -k1 -n> $2