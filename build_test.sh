#!/bin/bash

export PATH=\
/opt/buildout.python/bin:\
$PATH:

if [[ "$1" = "plone-4.3" ]]
then
    config=buildout-plone-4.3.cfg
    export WEBDAV_URL=http://localhost:$2/exist/webdav/db
fi

if [[ "$1" = "plone-5.0" ]]
then
    config=buildout-plone-5.0.cfg
    export WEBDAV_URL=http://localhost:$2/exist/webdav/db
fi


#virtualenv-2.7 .
pip install -U setuptools==7.0  
python bootstrap.py -c $config --setuptools-version 7.0 --version 2.2.5
bin/buildout -c $config
bin/test -s xmldirector.plonecore
##bin/coverage run bin/test
