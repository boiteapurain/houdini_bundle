# -*- coding: utf-8 -*-

name = "houdini_bundle"

version = "19.5.403.std.1.1"

description = "Houdini Side Fx package."

authors = ["It"]

variants = [["~python-3.9"]]

build_command = 'python {root}/build.py {install}'

release_command = 'python {root}/release.py {install}'


def commands():
    global system
    global env

    software = "19.5.403"

    if system.platform == "linux":
        # NO GPU
        env.HOUDINI_OCL_DEVICENUMBER.append(0)
        env.HOUDINI_OCL_DEVICETYPE.append("CPU")
        env.HOUDINI_USE_HFS_OCL.append(0)

        # HOUDINI BASIC CONFIG
        env.HFS.append(f"/opt/hfs{software}")

        # PATH
        env.PATH.append(f"/opt/hfs{software}/bin")
        env.PATH.append(f"/opt/hfs{software}/python/bin")

        # CMAKE CONFIG
        env.CMAKE_PREFIX_PATH.append(f"/opt/hfs{software}/toolkit/cmake")

