history | awk -F" " '
{   
    $1=""
    print$0
}
' | awk  '
$0 !~ /.txt|.json|.py|.p/ && $1 !~ /^git/ {
    linuxcommads[$1]=$1
    print > "output.txt"
}

$1 ~ /^git/{
    git[$0]=$0;
}
END{
    for (i in git){
        print i | "sort -k1 -n > gitcommands.txt"
    }
    for (i in linuxcommads){
        print i | "sort -k1 -n > linuxcommands.txt"
    }
}'