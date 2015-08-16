#!/bin/sh

if [ ! -f website-0.1.0-standalone.jar ]; then
  lein uberjar
  cp target/website-0.1.0-standalone.jar .
fi
java -jar website-0.1.0-standalone.jar
