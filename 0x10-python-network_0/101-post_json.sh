#!/bin/bash
# Script sends JSON POST request to URL first argument
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
