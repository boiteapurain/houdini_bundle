# -*- coding: utf-8 -*-

version = '19.0.561'


def commands():
    if system.platform == 'linux':

        ##########
        # NO GPU #
        ##########
        env.HOUDINI_OCL_DEVICENUMBER.append(0)
        env.HOUDINI_OCL_DEVICETYPE.append('CPU')
        env.HOUDINI_USE_HFS_OCL.append(0)

        ########
        # MAIN #
        ########

        # HOUDINI BASIC CONFIG
        env.HFS.append('/opt/hfs{version}')

        # PATH
        env.PATH.append('/opt/hfs{version}/bin')
        env.PATH.append('/opt/hfs{version}/python/bin')

        # HOUDINI_PATH
        env.PYTHONPATH.append('/opt/{version}/python/lib/python3.7')
        env.PYTHONPATH.append(
            '/opt/{version}/python/lib/python3.7/site-packages')

        #######
        # HDK #
        #######

        # CMAKE CONFIG
        env.CMAKE_PREFIX_PATH.append('/opt/hfs{version}/toolkit/cmake')

        # TO KEEP for no graphic card on laptop
        # HOUDINI_OCL_DEVICETYPE
        # HOUDINI_USE_HFS_OCL
        # HOUDINI_OCL_DEVICETYPE
        # HOUDINI_USE_HFS_OCL
