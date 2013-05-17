LGD is a [LinkedGeoData](http://linkedgeodata.org/) SPARQL query tool for [Quantum GIS](http://www.qgis.org/).

## Dependencies

* [RDFExtras](http://pypi.python.org/pypi/rdfextras)
* [sparql-client](http://pypi.python.org/pypi/sparql-client)

## Installation for OS X

Install dependencies

    pip install sparql-client rdfextras

Set PYTHONPATH environment variable

    sudo echo "setenv PYTHONPATH /usr/local/lib/python2.7/site-packages" >> /etc/launchd.conf

Download lgd plugin

    git clone git@github.com:StepanKuzmin/lgd.git

Create symlink

    ln -s lgd ~/.qgis/python/plugins/lgd
