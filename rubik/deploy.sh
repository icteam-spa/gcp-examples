#!/usr/bin/env bash


cd functions
case $1 in
    random)
        gcloud functions deploy rubik_random --entry-point random \
            --runtime python37 --trigger-http \
            --memory=128MB
            ;;
    validate)
        gcloud functions deploy rubik_validate --entry-point validate \
            --runtime python37 --trigger-http \
            --memory=128MB
            ;;
esac
cd -
