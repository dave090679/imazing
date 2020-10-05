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



class imazingOptionsWizardItem(uia.ListItem):
	def _get_name(self):
		l = list()
		for x in self.children:
			if x.role == controlTypes.ROLE_STATICTEXT:
				l.append(x.name)
		return " ".join(l);

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.ROLE_TREEVIEWITEM and obj.name == "IMazing.Sidebar.SidebarItem":
			clslist.insert(0, imazingtreeviewitem)
		elif obj.role == controlTypes.ROLE_LISTITEM and obj.name == "IMazing.Datasets.DeviceInfo.DeviceInfoButtonItem":
			clslist.insert(0, imazingdeviceinfobuttonitem)
		elif obj.role == controlTypes.ROLE_LISTITEM and obj.name in ["IMazing.StartWindow.StartWindowItem", "IMazing.Popover.DeviceItem", "IMazing.Wizards.Options.OptionsWizardItem", "IMazing.StartWindow.StartWindowDeviceItem", "IMazing.Wizards.QuickTransfer.CompatibleAppItem"]:
			clslist.insert(0, imazingOptionsWizardItem)
		elif obj.name == "":
			clslist.insert(0,remainingunlabeleduiaitem)