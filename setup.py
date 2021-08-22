import os
import shutil
import xml.etree.cElementTree as xml

home_path = os.path.expanduser("~")
config_path = ".config/xfce4/xfconf/xfce-perchannel-xml/"
file_name = "touchpad.sh"
file_xml_name = '%s/%sxfce4-keyboard-shortcuts.xml' % (home_path, config_path)


def editXML(filename):
    tree = xml.ElementTree(file=filename)
    root = tree.getroot()
    for child in root:
        if child.attrib['name'] == 'commands':
            for child1 in child:
                if child1.attrib['name'] == 'custom':
                    property = xml.SubElement(child1, "property")
                    property.set('name', 'TouchpadToggle')
                    property.set('type', 'string')
                    property.set('value', '%s/%s%s' % (home_path, config_path, file_name))

                    tree.write(filename)
                    break


shutil.copyfile("./%s" % file_name, "%s/%s%s" % (home_path, config_path, file_name))
os.chmod(r"%s/%s%s" % (home_path, config_path, file_name), 0o744)
editXML(file_xml_name)
