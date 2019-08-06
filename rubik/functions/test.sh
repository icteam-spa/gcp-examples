#!/usr/bin/env bash

target=$1
base_url=$2

case ${target} in
    rubik)
            cube=$(curl ${base_url}/rubik_random -H "Authorization: bearer $(gcloud auth print-identity-token)")
            echo '{"cube":' > request.txt
            echo ${cube} >> request.txt
            echo '}' >> request.txt
            valid=$(curl ${base_url}/rubik_validate --data @request.txt -H "Content-Type: application/json" -H "Authorization: bearer $(gcloud auth print-identity-token)")
            rm request.txt
            echo ${valid} | grep -c '{"valid": true}'
    ;;
esac