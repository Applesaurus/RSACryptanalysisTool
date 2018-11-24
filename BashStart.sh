#!/bin/bash

pyCryptControl="/cryptcontrol.py"

dirPath="$( cd "$( dirname "{BASH_SOURCE[0]}" )" && pwd )"
dirPath=$dirPath$pyCryptControl

python3 "$dirPath" "$@"
