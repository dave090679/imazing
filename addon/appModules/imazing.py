import appModuleHandler;
import api;
import NVDAObjects.UIA as uia;
import controlTypes
class imazingtreeviewitem(uia.TreeviewItem):
	def _get_name(self):
		l = list()
		for x in self.children:
			if x.role == controlTypes.ROLE_STATICTEXT:
				l.append(x.name)
		return " ".join(l);

class imazingdeviceinfobuttonitem(uia.ListItem):
	def _get_name(self):
		l = list()
		for x in self.children:
			if x.role == controlTypes.ROLE_BUTTON:
				l.append(x.description)
		return " ".join(l);

class imazingOptionsWizardItem(uia.ListItem):
	def _get_name(self):
		l = list()
		for x in self.children:
			if x.role == controlTypes.ROLE_STATICTEXT:
				l.append(x.name)
		return " ".join(l);

class imazingwhatsappmessagedisplayitem(uia.UIA):
	def _get_name(self):
		l = list()
		for x in self.firstChild.children:
			if x.role == controlTypes.ROLE_STATICTEXT:
				l.append(x.name)
		return " ".join(l);

class imazingddnacontactdetail(uia.UIA):
	def _get_name(self):
		l = list()
		l.append(self.children[0].firstChild.name);
		l.append(self.children[1].firstChild.value);
		return " ".join(l);

class imazingddnacontactgroup(uia.TreeviewItem):
	def _get_name(self):
		l = list()
		l.append(self.children[1].name);
		return " ".join(l);

class imazingddnacalendar(uia.TreeviewItem):
	def _get_name(self):
		l = list()
		l.append(self.children[0].name);
		return " ".join(l);


class imazingappmgrtab(uia.UIA):
	def _get_name(self):
		l = list()
		l.append(self.children[1].name);
		return " ".join(l);
class imazingprefsdataitem(uia.UIA):
	def _get_name(self):
		l = list()
		l.append(self.children[0].name);
		return " ".join(l);

class remainingunlabeleduiaitem(uia.UIA):
	def _get_name(self):
		s = '';
		l = list();
		for x in self.children:
			if x.role == controlTypes.ROLE_STATICTEXT:
				l.append(x.name)
		s = " ".join(l)
		if s == "":
			s = self.UIAElement.CachedAutomationId
		return s;

class imazingcomboboxitem(uia.ListItem):
	def _get_name(self):
		return self.firstChild.children[1].name


class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.ROLE_TREEVIEWITEM and obj.name in ["IMazing.Sidebar.SidebarItem", "IMazing.Datasets.Safari.SafariBookmarkDisplayItem"]:
			clslist.insert(0, imazingtreeviewitem)
		elif obj.role == controlTypes.ROLE_LISTITEM and obj.name == "IMazing.Datasets.DeviceInfo.DeviceInfoButtonItem":
			clslist.insert(0, imazingdeviceinfobuttonitem)
		elif obj.role == controlTypes.ROLE_LISTITEM and obj.name in ["IMazing.Wizards.Options.OptionsWizardItem", "IMazing.Shared.DeviceInfoDetailItem", "IMazing.Shared.OperationItem", "IMazing.BackupHistory.BackupHistoryItemDevice", "IMazing.BackupHistory.BackupHistoryItemArchive", "IMazing.Wizards.QuickTransfer.CompatibleAppItem"]:
			clslist.insert(0, imazingOptionsWizardItem)
		elif obj.role == controlTypes.ROLE_DATAITEM and obj.name == "IMazing.Datasets.WhatsApp.WhatsAppMessageDisplayItem":
			clslist.insert(0,imazingwhatsappmessagedisplayitem)
		elif obj.role == controlTypes.ROLE_DATAITEM and obj.name == "DDNA.ContactDetail":
			clslist.insert(0,imazingddnacontactdetail)
		elif obj.role == controlTypes.ROLE_TREEVIEWITEM and obj.name == "DDNA.ContactGroup":
			clslist.insert(0,imazingddnacontactgroup)
		elif obj.role == controlTypes.ROLE_TAB and "System.Windows.Controls.TabItem" in obj.name:
			clslist.insert(0,imazingappmgrtab)
		elif obj.role == controlTypes.ROLE_UNKNOWN and "IMazing.Preferences.BackupLocationItem" in obj.name:
			clslist.insert(0,imazingprefsdataitem)
		elif obj.role == controlTypes.ROLE_TREEVIEWITEM and obj.name == "DDNA.Calendar":
			clslist.insert(0,imazingddnacalendar)
		elif obj.role == controlTypes.ROLE_LISTITEM and obj.name == "System.Windows.Controls.ListBoxItem":
			clslist.insert(0,imazingcomboboxitem)
		elif obj.name == "":
			clslist.insert(0,remainingunlabeleduiaitem)
