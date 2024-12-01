"""
BEWARE!

The purpose of the code below is to help illustrate a general concept,
while relying on any inputs to be friendly and in an expected format.

Do not use this code as the basis for anything real.
"""

import json
import os
import sys

import jwt
import requests


def well_known_config(issuer):
    well_known_url = f"{issuer}/.well-known/openid-configuration"
    oidc_config = requests.get(well_known_url, timeout=10).json()

    jwks_uri = oidc_config["jwks_uri"]
    supported_algs = oidc_config["id_token_signing_alg_values_supported"]

    return jwks_uri, supported_algs


def header_lookup(token):
    key_id = jwt.get_unverified_header(token)["kid"]
    return key_id


def verify_decode(token, audience, jwks_uri, supported_algs, key_id):
    jwks_client = jwt.PyJWKClient(jwks_uri)
    signing_key = jwks_client.get_signing_key(key_id).key

    verified_claims = jwt.decode(
        token,
        key=signing_key,
        algorithms=supported_algs,
        audience=audience,
    )
    return verified_claims


def main():
    token = sys.argv[1]
    issuer = sys.argv[2]
    audience = sys.argv[3]

    jwks_uri, supported_algs = well_known_config(issuer)
    key_id = header_lookup(token)
    claims = verify_decode(token, audience, jwks_uri, supported_algs, key_id)

    with open(os.environ["GITHUB_OUTPUT"], mode="a", encoding="utf-8") as ghof:
        ghof.write(f"verified_claims={json.dumps(claims)}\n")


if __name__ == "__main__":
    main()
