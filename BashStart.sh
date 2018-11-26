#!/bin/bash

pyCryptControl="/cryptcontrol.py"

dirPath="$( cd "$( dirname "{BASH_SOURCE[0]}" )" && pwd )"
#replace dirname with the directory where cryptcontrol.py is located
dirPath=$dirPath$pyCryptControl

python3 "$dirPath" "$@"
