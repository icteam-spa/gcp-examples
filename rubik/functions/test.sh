#!/usr/bin/env bash

target=$1
base_url=$2

case ${target} in
    rubik)
            cube=$(curl ${base_url}/rubik_random)
            echo '{"cube":' > request.txt
            echo $cube >> request.txt
            echo '}' >> request.txt
    ;;
esac