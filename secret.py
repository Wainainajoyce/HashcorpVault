# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

import hvac
import sys

# Authentication
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='dev-only-token',
)

# Writing a secret
create_response = client.secrets.kv.v2.create_or_update_secret(
    path='mi-password',
    secret=dict(password='Githunguri1%'),
)

print('Secret written successfully.')

# Reading a secret
read_response = client.secrets.kv.read_secret_version(path='mi-password')

password = read_response['data']['data']['password']

if password != 'Githunguri1%':
    sys.exit('unexpected password')

print('Access granted!')