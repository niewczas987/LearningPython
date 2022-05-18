#internationalization class
class I18N():
    def __init__(self, language):
        if language == 'en': self.resourceLanguageEnglish()
        elif language == 'de': self.resourceLanguageGerman()
        else: raise NotImplementedError('Unsupported language')

    def resourceLanguageEnglish(self):
        self.title = 'Python Graphical User Interface'
        self.file = 'File'
        self.new = 'New'
        self.exit = 'Exit'
        self.help = 'Help'
        self.about = 'About'
        self.WIDGET_LABEL = ' Widget Frame '
        self.disabled = 'Disabled'
        self.unchecked = 'Unchecked'
        self.toggle = 'Toggled'
        self.colors = ['Blue','Gold','Red']
        self.colorsIn = ['in Blue', 'in Gold', 'in Red']
        self.labelsFrame = ' Labels within a frame '
        self.label2 = 'Label2'
        self.manageFiles = 'Manage files'
        self.browseTo = 'Browse to:'
        self.copyFileTo = 'Copy file to:'
        self.timeZones = "All Time Zones"
        self.localZone = "Local Zone"

    def resourceLanguageGerman(self):
        self.title = 'Python Grafische Benutzeroberflaeche'
        self.file = 'Datei'
        self.new = 'Neu'
        self.exit = 'Schliessen'
        self.help = 'Hilfe'
        self.about = 'Ueber'
        self.WIDGET_LABEL = ' Widgets Rahmen '
        self.disabled = 'Deaktiviert'
        self.unchecked = 'Nicht Markiert'
        self.toggle = 'Markieren'
        self.colors = ['Blau', 'Gold', 'Rot']
        self.colorsIn = ['in Blau', 'in Gold', 'in Rot']
        self.labelsFrame = ' Etiketten im Rahmen '
        self.chooseNumber = 'Waehle eine Nummer:'
        self.label2 = 'Etikette 2'
        self.manageFiles = ' Dateien Organisieren '
        self.browseTo = 'Waehle eine Datei... '
        self.copyFileTo = 'Kopiere Datei zu : '
        self.timeZones = "Alle Zeitzonen"
        self.localZone = "Lokale Zone"

#adding self testing
if __name__ == '__main__':
    language = 'de'
    inst = I18N(language)
    print(inst.title)

    language = 'en'
    inst = I18N(language)
    print(inst.title)