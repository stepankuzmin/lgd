# -*- coding: utf-8 -*-
"""
/***************************************************************************
 lgd
                                 A QGIS plugin
 A LinkedGeoData SPARQL query tool
                             -------------------
        begin                : 2013-01-20
        copyright            : (C) 2013 by Stepan Kuzmin
        email                : to.stepan.kuzmin@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "LinkedGeoData"


def description():
    return "A LinkedGeoData SPARQL query tool"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Stepan Kuzmin"

def email():
    return "to.stepan.kuzmin@gmail.com"

def classFactory(iface):
    # load lgd class from file lgd
    from lgd import lgd
    return lgd(iface)
