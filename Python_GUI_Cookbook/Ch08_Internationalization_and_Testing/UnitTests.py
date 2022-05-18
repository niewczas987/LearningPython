import unittest
from Python_GUI_Cookbook.Ch08_Internationalization_and_Testing.Language_Resources import I18N
from Python_GUI_Cookbook.Ch08_Internationalization_and_Testing.GUI_Refactored_Plus_Logging import OOP as GUI

class GuiUnitTests(unittest.TestCase):
    def test_TitleIsEnglish(self):
        i18n = I18N('en')
        self.assertEqual(i18n.title, 'Python Graphical User Interface')
    def test_TitleIsGerman(self):
        i18n = I18N('de')
        self.assertEqual(i18n.title, 'Python Grafische Benutzeroberflaeche')

class WidgetsTestEnglish(unittest.TestCase):
    def setUp(self):
        self.gui = GUI()
    def tearDown(self):
        self.gui = None
    def test_WidgetLabels(self):
        self.assertEqual(self.gui.i18n.file, 'File')
        self.assertEqual(self.gui.i18n.manageFiles, 'Manage files')
        self.assertEqual(self.gui.i18n.browseTo, 'Browse to:')

class WidgetsTestsGerman(unittest.TestCase):
    def setUp(self):
        self.gui = GUI()
        self.gui.i18n = I18N('de')
    def test_WidgetLabels(self):
        self.assertEqual(self.gui.i18n.file, "Datei")
        self.assertEqual(self.gui.i18n.manageFiles, ' Dateien Organisieren ')
        self.assertEqual(self.gui.i18n.browseTo, "Waehle eine Datei... ")
    def test_LabelFrameText(self):
        labelFrameText = self.gui.mighty['text']
        self.assertEqual(labelFrameText, "Mighty Python")
        self.gui.radVar.set(1) #programaticaly set the radio buton to 'red'
        self.gui.callBacks.radCall()
        labelFrameText = self.gui.mighty2['text']
        self.assertEqual(labelFrameText, "red")


if __name__ == '__main__':
    unittest.main()