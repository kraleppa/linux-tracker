#!/bin/bash

# shellcheck disable=SC2006
window=`xdotool getactivewindow`
pid=`xdotool getwindowpid $window`
# shellcheck disable=SC2006
D=`ps -e | awk '{if ($1 == '$pid') print $4}'`
echo $D