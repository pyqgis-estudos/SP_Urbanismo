# --------------------------------------------------------
#    SP_URBANISMO - QGIS plugins menu class
#
#    begin                : August 5, 2009
#    copyright            : (c) 2009 - 2012 by Michael Minn
#    email                : See michaelminn.com
#
#   SP_URBANISMO is free software and is offered without guarantee
#   or warranty. You can redistribute it and/or modify it 
#   under the terms of version 2 of the GNU General Public 
#   License (GPL v2) as published by the Free Software 
#   Foundation (www.gnu.org).
# --------------------------------------------------------

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMenu
from qgis.core import *

# from .mmqgis_dialogs import *

# ---------------------------------------------

class spurbanismo_menu:
	def __init__(self, iface):
		self.iface = iface
		self.spurbanismo_menu = None

	def spurb_add_submenu(self, submenu):
		if self.spurbanismo_menu != None:
			self.spurbanismo_menu.addMenu(submenu)
		else:
			self.iface.addPluginToMenu("&sp_urbanismo", submenu.menuAction())

	def initGui(self):
		# Uncomment the following two lines to have MMQGIS accessible from a top-level menu
		self.spurbanismo_menu = QMenu(QCoreApplication.translate("sp_urbanismo", "SP_Urbanismo"))
		self.iface.mainWindow().menuBar().insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.spurbanismo_menu)

		# Organização Submenu
		self.organizacao_menu = QMenu(QCoreApplication.translate("sp_urbanismo", "&Organização"))
		self.spurb_add_submenu(self.organizacao_menu)
		
		
		
		# Cadastro Submenu
		self.cadastro_menu = QMenu(QCoreApplication.translate("sp_urbanismo", "&Cadastro"))
		self.spurb_add_submenu(self.cadastro_menu)



		# IPTU Submenu
		self.iptu_menu = QMenu(QCoreApplication.translate("sp_urbanismo", "&IPTU"))
		self.spurb_add_submenu(self.iptu_menu)


	def unload(self):
		if self.spurbanismo_menu != None:
			self.iface.mainWindow().menuBar().removeAction(self.spurbanismo_menu.menuAction())
