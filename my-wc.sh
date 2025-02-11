#!/bin/bash
function my-wc() {
 if [ "$1" = "-c" ]; then
  python py-scripts/bytes.py "$2"
 fi
}