# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AGOLSearch
                                 A QGIS plugin
 This plugin search for data in ARCGIS Online
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-12-20
        copyright            : (C) 2018 by Geodienst University of Groningen
        email                : geodienst@rug.nl
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load AGOLSearch class from file AGOLSearch.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .agol_search import AGOLSearch
    return AGOLSearch(iface)
