import xml.etree.ElementTree as ET

root=ET.Element("root")
child=ET.SubElement(root,"child")
child.text="Bu xml formatında olusturulmus bir veridir."

tree=ET.ElementTree(root)
tree.write("dosya.xml")