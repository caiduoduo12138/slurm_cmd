#! /bin/bash
TARGET_DIR="/home/cai/project/slurm_cmd/module/"
for file in "$TARGET_DIR"/*.py
do
    pyinstaller -F -w $file
done
