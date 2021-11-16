class ListInstance:
    def __str__(self):
        return '<Instancja klasy %s, adres %s:\n%s>' % (self.__class__.__name__,  #nazwa klasy
                                                        id(self),               #adres
                                                        self.__attrnames())     #lista nazwa = wartosc
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tnazwa %s=%s\n'%(attr, self.__dict__[attr])
        return result

class ListInherited:
    def __str__(self):
        return '<Instancja klasy %s, adres %s:\n%s>' % (self.__class__.__name__,  #nazwa klasy
                                                        id(self),               #adres
                                                        self.__attrnames())     #lista nazwa = wartosc
    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\tname %s = <>\n'%attr
            else:
                result += '\tnazwa %s=%s\n'%(attr, getattr(self,attr))
        return result

class ListTree:
    def __str__(self):
        self.__visited ={}
        return '<Instancja klasy {0}, adres {1}:\n{2}{3}>'.format(self.__class__.__name__,  #nazwa klasy
                                                                    id(self),               #adres
                                                                    self.__attrnames(self,0), #lista nazwa = wartosc
                                                                    self.__listClass(self.__class__,4))
    def __listClass(self, aClass, indent):
        dots ='.' *indent
        if aClass in self.__visited:
            return '\n{0}<Klasa {1}:, adres {2}:, (patrz wyżej>\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listClass(c,indent+4) for c in aClass.__bases__)
            return '\n{0}<Klas {1}, adres {2}\n {3}{4}{5}>\n'.format(
                dots,
                aClass.__name__,
                id(aClass),
                self.__attrnames(aClass,indent),
                ''.join(genabove),
                dots)
    def __attrnames(self,obj,indent):
        spaces = ' '*(indent+4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces+'{0}=<>\n'.format(attr)
            else:
                result += spaces +'{0}={1}'.format(attr,getattr(obj,attr))
        return result
