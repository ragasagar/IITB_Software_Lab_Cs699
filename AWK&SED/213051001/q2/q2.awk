
BEGIN { OFS="\t"}
{
    split($0,a,"");
    year = "20"a[1]a[2];
    programme= a[3];
    department=a[4]a[5];
    serialno=a[6]a[7]a[8]a[9];

    program[0]="BTech";
    program[1]="MSc";
    program[3]="MTech"
    program[4]="PhD"
    program[9]="MBA"

    dept["01"]="Aerospace";
    dept["02"]="Chemical";
    dept["03"]="Chemistry"
    dept["04"]="Civil"
    dept["05"]="CSE"
    dept["09"]="Mathematics"
    dept["10"]="Mechanical"
    dept["12"]="Physics"
    dept["31"]="CSRE"
}
{
    print $0, year, program[programme], dept[department]
}
END{
    print "Total number of crushes: "NR

}