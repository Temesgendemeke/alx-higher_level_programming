#!/bin/bash
# sends request url
curl -o /dev/null -sw "%{http_code}" $1
