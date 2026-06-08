#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#
import subprocess
from extract_utils.fixups_blob import (
    BlobFixupCtx,
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

def blob_fixup_split(ctx: BlobFixupCtx, file, file_path: str, *args, **kwargs):
    subprocess.run(['split', '--bytes=49M', '-d', file_path, f'{file_path}.part'])

blob_fixups: blob_fixups_user_type = {
    'product/priv-app/MotCamera4/MotCamera4.apk': blob_fixup()
        .call(blob_fixup_split),
}  # fmt: skip

module = ExtractUtilsModule(
    'fogos',
    'motorola/motocamera',
    device_rel_path='vendor/motorola/motocamera',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
)

if __name__ == '__main__':
    ExtractUtils.device(module).run()
