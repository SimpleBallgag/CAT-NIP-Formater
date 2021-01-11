import random
import PySimpleGUI as sg
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
character = {
    "NAME" : "",
    "APPE" : "",
    "TRAI" : "",
    "WEAR" : "",
    "GEAR" : "",
    "SPEA" : "",
    "MENT" : "",
    "OCCU" : "",
    "SKIL" : "",
    "RELA" : "",
    "SITU" : "",
    "MOTI" : ""
    }

choices=list(attributes.keys())
sg.SetOptions(text_element_background_color='#6D7993', button_color=("#030314", "#6D7993"), background_color="#9099A2",font=("Helvetica", 20,))


catnip_column = [[sg.Text('Entity Name:'), sg.InputText(size = (20, 1), do_not_clear=True, key = "_NAME_"),

sg.Text("Entity Attribute"), sg.InputCombo(choices,size = (20, 1), key = "_ATTRIBUTE_")],
[sg.Text("Attribute Trait (seperate with a '/')"), sg.InputText(size = (20, 1), do_not_clear=True, key = "_TRAIT_"),
sg.Text("Trait Tags (seperate with a '/')"), sg.InputText(size = (20, 1), do_not_clear=True, key = "_TAGS_")],
                 [sg.Multiline("CAT<NIP> to appear here", size=(80,5), key = "_OUTPUT_", do_not_clear=True)],
                 [sg.Button("CATNIP!"),sg.Button("RESET"),sg.Button("SAVE EDIT")]]

layout = [[sg.Column(catnip_column, background_color="#6D7993")]]
  
window = sg.Window('CAT<NIP> Generator').Layout(layout)


first=1
output = "["
while True: 
    event, values = window.Read()
#    print(event)
#    print(values)
    if event is None or event == 'Exit':
        break
    if event == "CATNIP!" and values["_NAME_"] and values["_ATTRIBUTE_"]:
        try:
            if first:
                output = output+f'NAME<{values["_NAME_"]}>:{values["_NAME_"]}<first>;\n'
                first=0
            output = output+f'{attributes[values["_ATTRIBUTE_"]]}<{values["_NAME_"]}>:{values["_TRAIT_"]}<{values["_TAGS_"]}>.]'
            output = output.replace( '<>','')
            window.FindElement('_OUTPUT_').Update(output)
            output=output[:-2]
            output = output+';\n'
        except:
            pass
    if event == "RESET" :
        output = ""
        window.FindElement('_OUTPUT_').Update(output)
        output = "["
    if event == "SAVE EDIT" :
        output = values["_OUTPUT_"]
        window.FindElement('_OUTPUT_').Update(output)
        output=output[:-3]
        output = output+';\n'
      

window.Close()
