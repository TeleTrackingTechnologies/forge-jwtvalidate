# forge-jwtvalidate

This plugin is used to validate a JWT token against some public key. Useful for debugging issues around
jwt validation. With this you can determine if a jwt has been generated with the keypair you expect.

## Parameters

* JWT Token, available through parameter `-t` or `--token`. This should be the actual token needed to
validate.
* Public key file, available through the paramter `-p` or `--publickey`. This should be the path to the file.
* Algorithm, available through the parameter `-alg` or `--algorithm`. The default value is `RSA-256`

## How to install

`forge manage-plugins -a -r git@github.com:TeleTrackingTechnologies/forge-jwtvalidate.git -n forge-jwtgenerate`

## Example Usage

`forge jwtvalidate -t <some_jwt_token> -p some/path/to/key.pem`