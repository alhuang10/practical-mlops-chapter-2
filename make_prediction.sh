#!/bin/bash
# Usage: ./make_prediction.sh 'the soup was great'

if [ $# -eq 0 ]
then
    echo "No text supplied"
    echo "Example usage: ./make_prediction.sh 'the soup was great'"
    exit 1
fi

echo "String to predict: $1"

curl -X POST https://sentiment-ml-service.azurewebsites.net/sentiment \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "text=$1"