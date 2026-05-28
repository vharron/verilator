#!/usr/bin/env python3
# DESCRIPTION: Verilator: Verilog Test driver/expect definition
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of either the GNU Lesser General Public License Version 3
# or the Perl Artistic License Version 2.0.
# SPDX-FileCopyrightText: 2026 Google LLC
# SPDX-License-Identifier: LGPL-3.0-only OR Artistic-2.0

import vltest_bootstrap

test.scenarios('simulator')

if not test.have_solver:
    test.skip("No constraint solver installed")

# Allow the UNSIGNED warning which is expected for 'byte >= 0'
test.compile(verilator_flags2=['-Wno-UNSIGNED', '-LDFLAGS', '-lpthread', '-LDFLAGS', '-latomic'])

test.execute()

test.passes()
