# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.2)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\x75\
\x00\
\x00\x05\x0c\x78\x9c\xeb\x0c\xf0\x73\xe7\xe5\x92\xe2\x62\x60\x60\
\xe0\xf5\xf4\x70\x09\x62\x60\x60\x6a\x60\x60\x60\x7c\xc0\xc1\x06\
\x14\x31\xbd\x78\xe7\x09\x90\xe2\x2c\xf0\x88\x2c\x66\x60\xe0\x16\
\x06\x61\x46\x86\x59\x73\x24\x18\x18\x58\xf6\x79\xba\x38\x86\x54\
\xcc\x79\x7b\x90\x91\x17\xa8\xe4\xd0\x82\xef\xfe\xb9\x7c\xe6\x0b\
\x18\x46\xc1\x28\x18\x05\xa3\x60\x70\x03\x3b\x9e\x43\xef\x18\x18\
\x5f\x64\xcb\x2e\x05\xf1\x3c\x5d\xfd\x5c\xd6\x39\x25\x34\x01\x00\
\x27\x4a\x19\xdd\
"

qt_resource_name = b"\
\x00\x06\
\x07\x03\x7d\xc3\
\x00\x69\
\x00\x6d\x00\x61\x00\x67\x00\x65\x00\x73\
\x00\x0e\
\x07\x04\xfd\xe7\
\x00\x62\
\x00\x61\x00\x63\x00\x6b\x00\x67\x00\x72\x00\x6f\x00\x75\x00\x6e\x00\x64\x00\x2e\x00\x50\x00\x4e\x00\x47\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x12\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x12\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x7a\x6c\x15\x3e\x99\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
