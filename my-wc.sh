#!/bin/bash
function my-wc() {
 if [ "$1" = "-c" ]; then
  python py-scripts/bytes.py "$2"
 elif [ "$1" = "-l" ]; then
  python py-scripts/lines.py "$2"
 fi
}