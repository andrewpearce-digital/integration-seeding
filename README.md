# Sirius Integration Environment Seeding

This repository contains 2 python scripts.

One creates cases and documents by posting Set.xml files to Sirius Intgration.

## call_api_gateway.py

This script returns case data for a Sirius case ID.
```bash
python call_api_gateway.py
```

The script reads a list of case ids from a plaintext file called `uid_list`.

It makes an authenticated request to the sirius api gateway. 

The script reads account id, iam role and apigateway url from environment variables.

You can set these using direnv
```bash
direnv allow
```
 or by sourcing the .envrc file
```bash
source .envrc
```

The script uses your IAM user credentials to assume the appropriate role.

You can provide the script credentials using aws-vault
```
aws-vault exec identity -- python call_api_gateway.py 700000000047
```

## post_to_sirius.py


```bash
python post_to_sirius.py
```

The script reads a list of case ids from a plaintext file called `set_files_list`.