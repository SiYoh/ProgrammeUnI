from xml.dom import minidom
from parse import *




print("part 1")
#
doc = minidom.parse('/XML/test.xml')

doc.childNodes

if doc.childNodes[0].hasChildNodes():
#	
	root = doc.documentElement
	
	root.childNodes
	root.firstChild
	root.lastChild
	current = root.firstChild
	while current:
	    print(current)
#	
	    current = current.nextSibling


print("Part 2")
root
root.firstChild.parentNode
root.firstChild.isSameNode(root.childNodes[0])
for element in root.getElementsByTagName('contact'):
    print(element)
for element in root.getElementsByTagName('programming'):
   print(element)
# ELEMENT_NODE, ATTRIBUTE_NODE, TEXT_NODE,
# CDATA_SECTION_NODE, ENTITY_NODE, 
# PROCESSING_INSTRUCTION_NODE, COMMENT_NODE, 
# DOCUMENT_NODE, DOCUMENT_TYPE_NODE, NOTATION_NODE
root.nodeType == minidom.Node.ELEMENT_NODE
root.nodeName
root.firstChild.nodeName
root.nodeValue
root.firstChild.nodeValue
root.firstChild.data
root.hasAttributes()
root.childNodes[1].hasAttributes()
root.firstChild.attributes
attributes = root.childNodes[1].attributes
attributes
c = root.childNodes[1]
c.getAttribute('name')
c.getAttributeNode('name')
attributes.items()
attributes.keys()
attributes.values()
for a in attributes.values():
    print(a.nodeType, a.nodeName, a.nodeValue)
attrs = root.childNodes[1].attributes
for idx in range(0, attrs.length):
    a = attrs.item(idx)
    print('(' + a.name + ')')
    print(a.nodeType, a.nodeName, a.nodeValue)



print("part 3")

newdoc = minidom.Document()
newdoc
newroot = newdoc.createElement('root')
rootattr = newdoc.createAttribute('name')
rootattr.nodeValue = 'foo'

textnode = newdoc.createElement('sometext')
text = newdoc.createTextNode('this node\ncontains text')
textnode.appendChild(text)
comment = newdoc.createComment('a very usefull comment')
newdoc.appendChild(newroot)
textnode.appendChild(text)
newroot.appendChild(textnode)
newroot.insertBefore(comment, textnode)
newroot.setAttribute('usefull', 'nop')
newroot.setAttributeNode(rootattr)
try:
    old = root.removeChild(root.firstChild)
    old.unlink()
except ValueError: print('failed')
root.firstChild
root.firstChild.removeAttribute('firstname')
newdoc.toxml()
print(newdoc.toprettyxml())







# Vulgariser le langage !!!!!!!!!!!!!!!!!!!
#def Categorize(choix):
#	if choix == 'o' or choix == 'O' or choix == 'oui' or choix == 'y' or choix == 'yes' or choix == '1' or choix == 'Y' :
#		cle = input("indiquer la catégorie de la donnée :")
#	elif choix == 'non' or choix == 'n' or choix == 'no' or choix == 'N' choix == '0' or :
#		pass
#	else : 
#		print("Je ne comprends pas votre réponse.\n\nVeuillez réessayer s'il vous plait")
#	return cle
#
##Balise ouvrante
#def BaliseOuvrante(Balise):
#	print("<")
#	Balise
#	choix = input("Voulez vous rajouter une catégorie ? oui ou non")
#	Categorize(choix)
#	print(">")
#
#
#
##Balise fermante
#def BaliseFermante(Balise):
#	print("</")
#	Balise
#	print(">")
#
##création du balisage XLM
#def IndexationXLM(Data):
#	Balise = input("Indiquer le nom de la balise :")
#	BaliseOuvrante(Balise)
#	#
#
#	inscriptionData()
#	BaliseFermante(Balise)
#
#
## une fois l'indexation des données XML au sein 
#