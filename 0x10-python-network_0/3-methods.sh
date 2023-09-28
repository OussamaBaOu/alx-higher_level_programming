#!/bin/bash
# Script that takes in URL and displays all acceptable HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
