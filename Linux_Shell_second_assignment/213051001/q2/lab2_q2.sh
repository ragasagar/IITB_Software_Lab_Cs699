

echo "$#"
sum=0;

for item in "${@}"; do
    value=$((item*item*item))
    sum=`expr $sum + $value`
done

echo "$sum"