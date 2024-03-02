#!/bin/bash
# sends a GET request to the URL
curl -X OPTIONS $1 | awk '/Allow/ {print substr($0, index($0, ":") + 2)}'