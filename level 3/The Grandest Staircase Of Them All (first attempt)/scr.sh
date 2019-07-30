#!/usr/bin/env bash

url="http://api.wolframalpha.com/v2/query?appid=APHHPH-GA3U5ULJWP&input=PartitionsQ("

n=1

while :
do
	result=`curl -X GET "$url$n)" 2>/dev/null | egrep -e "<plaintext>[0-9]+</plaintext>" -o | egrep -e "[0-9]+" -o`
	echo $n $result >> res.file
	# sleep 1s
	n=$(($n + 1))
done
