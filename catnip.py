import random
import PySimpleGUI as sg
from anytree import Node, RenderTree
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

sg.Text("Entity Attribute"), sg.InputCombo(choices,size = (20, 1), key = "_ATTRIBUTE_")],
[sg.Text("Attribute Trait (seperate with a '/')"), sg.InputText(size = (20, 1), do_not_clear=True, key = "_TRAIT_"),
sg.Text("Trait Tags (seperate with a '/')"), sg.InputText(size = (20, 1), do_not_clear=True, key = "_TAGS_")],
                 [sg.Multiline("CAT<nip> to appear here", size=(80,15), key = "_OUTPUT_", do_not_clear=True)],
                 [sg.Button("CATnip!"),sg.Button("RESET")]]

layout = [[sg.Column(catnip_column, background_color="#6D7993")]]
  
window = sg.Window('CAT<nip> Generator').Layout(layout)


output=""
while True: 
    event, values = window.Read()
#    print(event)
#    print(values)
    if event is None or event == 'Exit':
        break
    if event == "CATnip!" and values["_NAME_"] and values["_ATTRIBUTE_"]:
        try:
            output=""

            for pre, fill, node in RenderTree(CATnip):
                if node.name==attributes[values["_ATTRIBUTE_"]] and values["_TRAIT_"] not in str(node.children):
                    Node(values["_TRAIT_"],parent=node)


            for pre, fill, node in RenderTree(CATnip):
                if node.name==values["_TRAIT_"]:
                    Node(values["_TAGS_"],parent=node)

           #Start of Output Logic
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
            window.FindElement('_OUTPUT_').Update(output)
            print(RenderTree(CATnip))

        except:
            pass
    if event == "RESET" :
        output = ""
        CATnip = Node("NAME",parent=None)
        for i in attributes.values():
            Node(i, parent=CATnip)
        window.FindElement('_OUTPUT_').Update(output)

window.Close()
