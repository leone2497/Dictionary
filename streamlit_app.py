#chiave:streamlit run ./Dictionary.py
import streamlit as st
import random

# Define the dictionaries
English = {
    "brittle": "friabile",
    "whizz":"sfrecciare",
    "dredge up": "rivangare",
    "declutter": "riordinare",
    "heckle":"infastidire",
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
    "plum":"prugna,succoso"
}
Spanish = {
    "valia": "valore",
    "vispera": "vigilia",
    "arrasar": "stravincere",
    "basura":"garbage",
    "agotar":"use up, drain, wear out",
    "pesadilla": "nightmare",
    "jubilado":"retired",
    "empresariado":"businessman",
    "pie":"foot",
    "advertir":"warn",
    "apenas":"barely, as soonn as"
    
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
