#!/bin/sh

set -e

java Factorial 5 | grep -q -w 120
