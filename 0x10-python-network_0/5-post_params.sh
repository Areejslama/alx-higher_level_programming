#!/bin/bash
# this script to use post method
curl -s -L -d "email:test@gmail.com" "subject:I will always be here for PLD" "$1"
