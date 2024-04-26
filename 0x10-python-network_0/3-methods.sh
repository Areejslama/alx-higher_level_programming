#!/bin/bash
#this script to display methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
