#!/bin/sh

step=5
case $1 in
  -) amixer -D pulse sset Master "$step"%-;;
  +) amixer -D pulse sset Master "$step"%+;;
  t) amixer -D pulse sset Master toggle;;
esac
