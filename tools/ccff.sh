#!/bin/bash

# ccf (Create Class Folder and File)

class_name="aula$1"

mkdir $class_name && touch "$class_name/$class_name.py"


