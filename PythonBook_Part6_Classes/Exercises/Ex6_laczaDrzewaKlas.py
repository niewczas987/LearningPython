class ListInstance:
    def __str__(self):
        return '<Instancja klasy %s(%s), adres %s:\n%s'% (
            self.__class__.__name__,
            self.__supers(),
            id(self),
            self.__attrnames()
        )
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tnazwa %s=%s\n'%(attr, self.__dict__[attr])
        return result
    def __supers(self):
        names =[]
        for super in self.__class__.__bases__:
            names.append(super.__name__)
        return ', '.join(names)
    
