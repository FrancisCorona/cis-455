# Merkle Hash Tree for Integrity Check

## Overview
This project implements a Merkle Hash Tree using MD5 hashing to verify the integrity of multiple files. The Top Hash changes if any file is modified demonstrating data integrity.

## Output

Initial Top Hash:

![Initial Top Hash](./images/initial-check.png)

Modified Top Hash after changing a file:
  
![Modified Top Hash](./images/modified-check.png)

## Running the Program
To compute the Top Hash use the following command:
```bash
python3 merkle-hash-tree.py test-files/*
