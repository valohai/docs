#!/bin/bash
set -xeuo pipefail

aws s3 sync --delete --acl public-read build/dirhtml/ s3://docs.valohai.com/
aws cloudfront create-invalidation --distribution-id=E3U5DQUSY4EOFH --paths '/*'
