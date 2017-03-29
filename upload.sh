#!/bin/bash
set -xeuo pipefail

aws s3 sync --delete --acl public-read build/html/ s3://docs.valohai.com/
