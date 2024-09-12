#chiave:streamlit run ./Dictionary.py
import streamlit as st
import random

# Define the dictionaries
English = {
    "brittle": "friabile",
    "disgress":"divagare",
    "harzardous":"pericolos",
    "berate":"rimproverare",
    "sink in":"essere assorbito",
    "deformity":"deformità",
    "write up":"scrivere una critica",
    "stuck-up":"pieno di sè",
    "sound":"saggio",
    "supper":"dinner",
    "rocky":"rocciosos, burrascoso",
    "wither":"appassire",
    "sardonic":"beffardo",
    "let off":" lasciare correre, permettere a di evitare qlc",
    "shuffle":"scompigliare",
    "scold":"berate",
    "wail":"pianto, piangere",
    "deplete":"svuotare, esaurire",
    "pelvis":"bacino",
    "whizz":"sfrecciare",
    "shiver":"rabbrividire, tremolio",
    "prowess":"abilità",
    "outvote":"ricevere più voti",
    "gore":"sangue",
    "precient":"distretto di polizia",
    "commendable":"encomiabile",
    "skim off":"fare la cresta",
    "lumber":"muoversi pesantemente",
    "dank":"umido, moist",
    "bedazzle":"accecare",
    "stakeout":"appostamento, punto di sorveglianza",
    "squish":"spremere, strizzare",
    "forefront":"ribalta, riflettori",
    "dredge up": "rivangare",
    "declutter": "riordinare",
    "heckle":"infastidire",
    "thwart":"sventare",
    "derogatori":"dispregiativo",
    "see-through":"trasparente",
    "roll in":"presentarsi, comparire",
    "pelt":"bombardare, picchiettare",
    "arilock":"intercapedine",
    "ludicrus":"assurdo, ridicolo",
    "titillate":"sollecitare, titillare",
    "scurry":"vuoversi freneticamente",
    "hopscotch":"gioco della campana",
    "overrun":"invadere,eccedere,oltrepassare",
    "deadbolt":"serratura di sicurezza",
    "devoid":"privo",
    "crop up":"show up",
    "come about":"succedere",
    "headstrong":"caparbio",
    "abide":"stick to, stand for",
    "fester":"inasprirsi",
    "toggle":"azionare,far scattare",
    "brandish":"brandire",
    "scrutiny":"esame minuzioso",
    "scuttle":"affondare (proposta),muoversi freneticamente",
    "frown upon":"biasimare, esprimere la propria contrairietà",
    "phase-out":"eliminazione progressiva",
    "phase out":"eliminare progressivamente",
    "bedrock":"base, fondamento",
    "oftentimes":"frequentemente",
    "momentum":"impeto",
    "dovetail":"incastarsi,andare alla perfezione",
    "hitch":"contrattempo",
    "hiccup":"contrattempo",
    "pundit":"critico",
    "plum":"prugna,succoso",
    "reprehensible":"riprovevole",
    "flashpoint":"luogo di crisi;punto di rottura",
    "caterpillar":"bruco",
    "lookout":"punto di osservazione,osservatorio",
    "ad-lib":"improvvisare",
    "dampen":"inumidire,smorzare",
    "prawn":"shrimp",
    "slum":"bassifondi",
    "click with":"andare d'accordo"
}
Spanish = {
    "valia": "valore",
    "basura":"spazzatura",
    "arrollar":" drag underneath, knock down, crush",
    "baja":"decrease in price, sick leave",
    "arrollador":"overwhelming",
    "tasa":"fee",
    "a la baja":"on decline",
    "repercusiòn":"consequence",
    "ademàs":"in addition, also",
    "decepcionar":"disappoint",
    "marcha":"progress, walk",
    "aliviar":"alleviate, relieve, ease",
    "vispera": "vigilia",
    "rebaja":"reduction",
    "recortar":"cut",
    "estimular":"encourage",
    "deprimir":"depress",
    "equivocarse":"get mistaken",
    "restrasar":"postpone, delay",
    "paro":"strike",
    "entorpecer":"hinder",
    "exigir":" require, ask",
    "mantener":"keep",
    "convenio":"agreement",
    "arrasar": "stravincere",
    "basura":"garbage",
    "escalòn":"step",
    "subvenciòn":"subcidy, grant",
    "caro":"expensive",
    "huelga":"paro",
    "tripulante":"crew member",
    "cese":"stoppage",
    "ablandar":"ammorbidire, rendere più tenero",
    "marisco":"frutti di mare",
    "agotar":"use up, drain, wear out",
    "pesadilla": "nightmare",
    "jubilado":"retired",
    "empresariado":"businessman",
    "pie":"foot",
    "advertir":"warn",
    "apenas":"barely, as soonn as",
    "descansar":"riposarsi",
    "situar":"collocare  (anche figurativo)",
    "ingreso":"entrata, reddito",
    "informativo":"news",
    "ancho":"width, wide",
    "librar":"liberarsi, be spared",
    "producirse":"happen",
    "suponer":"suppose, mean",
    "alcance":"range",
    "dañar":"damage, harm",
    "huir":"flee",
    "desplazar":"move",
    "alcanzar":"reach, achieve",
    "cuyos":"whose",
    "involucrar":"involve",
    "rostro":"face, image",
    "reajuste":"reform, readjustment",
    "asediar":"besiege",
    "destrozar":"destroy",
    "entorno":"enviroment, surrounding",
    "recelo":"mistrust",
    "considerar":"consider, evaluate",
    "debilitar":"weaken",
    "sumamente":"esxtremely",
    "ficha":"card, file"
}

def get_random_word(dictionary):
    if not dictionary:
        raise ValueError("The dictionary is empty")
    return random.choice(list(dictionary.keys()))

# Title of the app
st.title("My Dictionary App")

# Sidebar for dictionary selection
st.sidebar.title("Dictionaries")
dictionary_type = st.sidebar.selectbox("Choose a dictionary", ["English", "Spanish"])

# Sidebar for action selection
st.sidebar.title("Actions")
action = st.sidebar.selectbox(
    "What would you like to do?",
    ["Lookup", "Add New Word", "Random Word"]
)

# Reference the correct dictionary based on selection
selected_dictionary = English if dictionary_type == "English" else Spanish

# Lookup functionality
if action == "Lookup":
    st.subheader("Lookup a Word")
    word = st.text_input("Enter a word to look up:").strip().lower()
    
    if word:
        definition = selected_dictionary.get(word)
        if definition:
            st.write(f"**{word.capitalize()}:** {definition}")
        else:
            st.write(f"Sorry, the word '{word}' was not found in the dictionary.")

# Add new word functionality
elif action == "Add New Word":
    st.subheader("Add a New Word")
    new_word = st.text_input("Enter the word you want to add:").strip().lower()
    new_definition = st.text_area("Enter the definition for the new word:")
    
    if st.button("Add Word"):
        if new_word in selected_dictionary:
            st.write(f"The word '{new_word}' already exists in the dictionary.")
        else:
            selected_dictionary[new_word] = new_definition
            st.write(f"The word '{new_word}' has been added to the {dictionary_type} dictionary.")

# Random word functionality
elif action == "Random Word":
    st.subheader("Random Word")
    if st.button("Get Random Word"):
        random_word = get_random_word(selected_dictionary)
        st.write(f"**{random_word.capitalize()}:** {selected_dictionary[random_word]}")
