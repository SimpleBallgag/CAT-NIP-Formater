import random
import PySimpleGUI as sg
import copy
from anytree import Node, RenderTree

def display(CATnip):
    output=""
    for pre, fill, node in RenderTree(CATnip):
        if node.parent==CATnip:
            output=output+("%s%s%s%s%s" %  ("$$$",node.name,'<',values["_NAME_"],'>'))
        elif node.parent in CATnip.children:
            output=output+("%s%s" %  ("/",node.name))
        elif node.is_root==True:
            output=output+("%s%s%s%s%s" %  ("[",node.name,'<',values["_NAME_"],'>'))
        else:
            output=output+("%s%s%s" %  ("<",node.name,'>'))

    output=output.replace(values["_NAME_"]+">/",values["_NAME_"]+'>:')
    output=output.replace("$$$",';\n')
    output=output.replace("><",'/')
    output=output.replace("<>",'')
    thelist=output.split('\n')
    output=""
    for item in thelist:
        if len(item)>len(values["_NAME_"])+7:
            output=output+'\n'+item
    output=output[1:-1]+'.]'
    return output




attributes={
    "Appearance" : "APPE", 
    "Traits" : "TRAI", 
    "Wearing" : "WEAR", 
    "Gear" : "GEAR", 
    "Speaking" : "SPEA", 
    "Mentality" : "MENT", 
    "Occupation" : "OCCU", 
    "Skills" : "SKIL", 
    "Relationships" : "RELA", 
    "Situation" : "SITU", 
    "Motivations" : "MOTI"
    }

CATnip = Node("NAME",parent=None)
for i in attributes.values():
  Node(i, parent=CATnip)

choices=list(attributes.keys())
sg.SetOptions(text_element_background_color='#6D7993', button_color=("#030314", "#6D7993"), background_color="#9099A2",font=("Helvetica", 20,))

catnip_column = [[sg.Text('Entity Name:'), sg.InputText(size = (20, 1), do_not_clear=True, key = "_NAME_"),

sg.Text("Entity Attribute"), sg.InputCombo(choices,size = (20, 1), key = "_ATTRIBUTE_"),sg.Text("Insert..."),sg.Button("CAT<nip>")],
[sg.Text("Attribute Trait (seperate with a '/')"), sg.InputText(size = (20, 1), do_not_clear=True, key = "_TRAIT_"),
sg.Text("Trait Tags (seperate with a '/')"), sg.InputText(size = (20, 1), do_not_clear=False, key = "_TAGS_")],
                 [sg.Multiline("CAT<nip> to appear here", size=(80,15), key = "_OUTPUT_", do_not_clear=False)],
                 [sg.Button("RESET")],[sg.Button("UNDO")]]

layout = [[sg.Column(catnip_column, background_color="#6D7993")]]
  
window = sg.Window('CAT<nip> Generator').Layout(layout)

undolist=[]
while True: 
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if event == "CAT<nip>" and values["_NAME_"] and values["_ATTRIBUTE_"]:
        try:
            undolist.append(copy.deepcopy(CATnip))
            output=""
            for pre, fill, node in RenderTree(CATnip):
                if node.name==attributes[values["_ATTRIBUTE_"]] and values["_TRAIT_"] not in str(node.children):
                    Node(values["_TRAIT_"],parent=node)
            for pre, fill, node in RenderTree(CATnip):
                if node.name==values["_TRAIT_"]:
                    Node(values["_TAGS_"],parent=node)
            #Start of Output Logic
            output=display(CATnip)
            window.FindElement('_OUTPUT_').Update(output)
        except:
            pass
    if event == "RESET" :
        output = ""
        undolist.append(copy.deepcopy(CATnip))
        CATnip = Node("NAME",parent=None)
        for i in attributes.values():
            Node(i, parent=CATnip)
        window.FindElement('_OUTPUT_').Update(output)
    if event == "UNDO" and len(undolist)>0:
        try:
            CATnip = undolist.pop()
            output=display(CATnip)
            window.FindElement('_OUTPUT_').Update(output)
        except:
            pass
window.Close()
