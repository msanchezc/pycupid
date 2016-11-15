import os
import sys
import subprocess
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from distutils.extension import Extension
from distutils.command.build_ext import build_ext
try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

WRAPPER_SRC_DIR = 'pycupid'
CUPID_SRC_DIR = os.path.join('cupid', 'src')

class custom_build_ext(build_ext):
    def run(self):
        # Build CUPID
        #subprocess.call(['make'])
        # Then, build wrapper around it.
        build_ext.run(self)

cupid_sources = [
    'cupidcfaddpixel.c',
    'cupidcfdeleteps.c',
    'cupidcferode.c',
    'cupidcffreeps.c',
    'cupidcfidl.c',
    'cupidcflevels.c',
    'cupidcfmakeps.c',
    'cupidcfnebs.c',
    'cupidcfscan.c',
    'cupidcfxfer.c',
    'cupidclumpfind.c',
    'cupidconfigD.c',
    'cupidconfigI.c',
    'cupidconfigrms.c',
    'cupiddefminpix.c',
    'cupidfellwalker.c',
    'cupidfwjoin.c',
    'cupidfwmain.c',
    'cupidfwpixelsets.c',
    'cupidgaussclumps.c',
    'cupidgccalcf.c',
    'cupidgccalcg.c',
    'cupidgcchisq.c',
    'cupidgcdump.c',
    'cupidgcfindmax.c',
    'cupidgcfit.c',
    'cupidgclistclump.c',
    'cupidgcmodel.c',
    'cupidgcndfclump.c',
    'cupidgcprofwidth.c',
    'cupidgcsetinit.c',
    'cupidgcupdatearrays.c',
    'cupidndfclump.c',
    'cupidrca.c',
    'cupidrca2.c',
    'cupidrcheckface.c',
    'cupidrcopyline.c',
    'cupidredges.c',
    'cupidreinhold.c',
    'cupidrfill.c',
    'cupidrfillclumps.c',
    'cupidrfillline.c',
    'cupidrinitedges.c',
    'cupidsumclumps.c',
]

ext = '.pyx' if USE_CYTHON else '.c'

wrapper_sources = [source + ext for source in ['pycupid',]]

wrapper_sources = [os.path.join(WRAPPER_SRC_DIR, s) for s in wrapper_sources]
cupid_sources = [os.path.join(CUPID_SRC_DIR, s) for s in cupid_sources]

ext_sources = wrapper_sources + cupid_sources

extensions = [
    Extension(
        "pycupid.pycupid",
        ext_sources,
        include_dirs = [os.path.join("star", "include"), os.path.join("cupid", "include")],
        library_dirs = [os.path.join("star", "lib")],
        extra_link_args = ["-Wl,-rpath=" + os.path.join("$ORIGIN", "star", "lib")],
        libraries = [
            "ast", 
            "err_standalone", 
            "hds", 
            "ndf", 
            "pda",
            # AST
            "ast_pal",
            "ast_grf_2.0",
            "ast_grf_3.2",
            "ast_grf_5.6",
            "ast_grf3d",
            "ast_pass2",
            "ast_err",
            "m",
            # MERS
            "chr",
            "emsf",
            "ems",
            "cnf",
            "starmem",
            "pthread",
            "starutil",
            # HDS
            "hdsf",
            "hds",
            # NDF
            "psx",
            "ary",
            "prm",
            "prm_a",
            "ast_ems",
        ],
    ),
]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(
    name = 'pycupid',
    version = '0.1.0',
    author = u'Manuel Sánchez',
    author_email = 'manuel.sanchez@linux.com',
    packages = ['pycupid'],
    package_data = {'pycupid': ['star/lib/*',]},
    url = 'https://github.com/msanchezc/pycupid',
    description = 'Python wrappers for Starlink\'s CUPID package',
    ext_modules = extensions,
    cmdclass = {
        'build_ext': custom_build_ext,
    },
    install_requires = {
        'numpy >= 1.11.2',
    }
)