import appModuleHandler;
import api;
import NVDAObjects.UIA as uia;
import controlTypes
class imazingprofileeditor_comboboxitem(uia.ListItem):
	def _get_name(self):
		return self.firstChild.name
class imazingprofileeditor_generic(uia.UIA):
	def _get_name(self):
			return self.UIAElement.CachedAutomationId

class imazingprofileeditor_sectionitem(uia.ListItem):
	def _get_name(self):
		l = list()
		for x in self.children:
			if x.role == controlTypes.ROLE_STATICTEXT and x.name:
				l.append(x.name)
		return ";".join(l)



class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.ROLE_LISTITEM and obj.name in ["iMazing_Profile_Editor.View_Controllers.Value_Converters.ComboBoxStringItem"]:
			clslist.insert(0, imazingprofileeditor_comboboxitem)
		elif obj.role == controlTypes.ROLE_LISTITEM and obj.name in ["iMazing_Profile_Editor.Sections.Section"]:
			clslist.insert(0, imazingprofileeditor_sectionitem)
		elif obj.name == "":
			clslist.insert(0,imazingprofileeditor_generic)
