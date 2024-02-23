#!/bin/bash

# gacp (git add, git commit, git push)

git add . && git commit -m "$1" && git push -u origin main