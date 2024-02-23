#!/bin/bash

# ccf (Create Class Folder and File)

section_number=$1
class_number="aula$2"

aulas_folder="./aulas"
section= ls $aulas_folder | grep $section_number
mkdir $aulas_folder/$section/$class_number && touch "$aulas_folder/$section/$class_number/$class_number.py"