#!/bin/bash
for DIR in posts/*/ ; do
  quarto render $DIR
done
