import streamlit as st
import spacy
from spacy import displacy

def load_text_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().splitlines()

    # Définir la couleur pour chaque type d'entité
entity_colors = {
    'PER': "#84D41D",
    'ORG': "#91BACF",
    'LOC': "#BF5C00",
    'DATE': "#F2E783",
    'MISC': "White"
}


def main():
    # Chargement du modèle SpaCy
    ner_model = spacy.load("C:\\Users\\Don Arhona\\Desktop\\IA_Competition\\NerApp\\ModelNER")

    # Liste des noms de fichiers
    file_options = {
        "XIBAR": False,
        "TAGGAT": False,
        "LIFESS": False
    }

    # Exploration de données
    st.title("Named Entity Recognition in Wolof")

    taches = ['--Choix--', 'Saisir un exemple de texte en wolof', 'Sélectionnez un exemple de phrase en wolof']

    choix = st.sidebar.selectbox("Sélectionner une activité", taches)

    if choix == '--Choix--':
        # Afficher la définition NER
        st.subheader("Définition de NER (Named Entity Recognition)")
        st.write("La reconnaissance d'entités nommées (NER) est une technique de traitement du langage naturel qui consiste à identifier et classer les entités nommées telles que les noms de personnes, d'organisations, de lieux, de dates, etc. dans un texte.")
      
    elif choix == 'Saisir un texte en wolof':
        # Zone de texte
        user_input = st.text_area("**Entrez la phrase en wolof:**", help="La zone de texte s'ajustera automatiquement à la taille du texte.")

        # Ajout d'une variable pour garder en mémoire le résultat
        result = None

        # Bouton "Soumettre"
        if st.button("Soumettre"):
            # Utilisation du modèle SpaCy NER pour effectuer le traitement sur user_input
            doc = ner_model(user_input)
            
            # Utilisation du modèle SpaCy NER pour effectuer le traitement sur user_input
            doc = ner_model(user_input)

            # Créer une liste pour regrouper les entités de même étiquette consécutives
            grouped_entities = []
            current_entity = ""

            for ent in doc.ents:
                entity_type = ent.label_

                if entity_type == current_entity:
                    # Ajoutez l'entité au groupe actuel
                    grouped_entities[-1][0] += f", {ent.text}"
                else:
                    # Créez un nouveau groupe pour l'entité
                    grouped_entities.append([ent.text, entity_type])
                    current_entity = entity_type

            # Affichage de la phrase formatée
            formatted_text = displacy.render(doc, style='ent', options={'colors': entity_colors})
            st.markdown(formatted_text, unsafe_allow_html=True)

            # Affichage des entités nommées détectées
            st.markdown('<span style="font-weight:bold; text-decoration: underline; color:#132959;">Entités nommées détectées :</span>', unsafe_allow_html=True)
            for entity_text, entity_type in grouped_entities:
                color = entity_colors.get(entity_type, "black")
                st.markdown(f'<span style="background-color: {color}; color: black; padding: 6px; border-radius: 10px;"><strong>{entity_text} ({entity_type})</strong></span>', unsafe_allow_html=True)


    elif choix == 'Sélectionnez un exemple de phrase en wolof':
        st.subheader("Sélectionnez un fichier :")
        for option, checked in file_options.items():
            file_options[option] = st.checkbox(option, checked)
        
        selected_files = [option for option, checked in file_options.items() if checked]

        if selected_files:
            examples = []
            for selected_file in selected_files:
                examples += load_text_file(f"{selected_file}.txt")

            # Sélectionner un exemple de phrase à partir de la liste
            selected_example = st.selectbox("Sélectionnez un exemple de phrase en wolof :", examples)

            # Zone de texte
            user_input = st.text_area("Entrez la phrase en wolof :", selected_example, help="La zone de texte s'ajustera automatiquement à la taille du texte.")

            # Ajout d'une variable pour garder en mémoire le résultat
        result = None

        # Bouton "Submit"
        if st.button("Soumettre"):
            # Utilisation du modèle SpaCy NER pour effectuer le traitement sur user_input
            doc = ner_model(user_input)
            
            # Créez une liste pour regrouper les entités de même étiquette consécutives
            grouped_entities = []
            current_entity = "s"
            
            for ent in doc.ents:
                entity_type = ent.label_
                
                if entity_type == current_entity:
                    # Ajoutez l'entité au groupe actuel
                    grouped_entities[-1][0] += f", {ent.text}"
                else:
                    # Créez un nouveau groupe pour l'entité
                    grouped_entities.append([ent.text, entity_type])
                    current_entity = entity_type
            
            # Affichage de la phrase formatée
            formatted_text = displacy.render(doc, style='ent', options={'colors': entity_colors})
            st.markdown(formatted_text, unsafe_allow_html=True)
            
            # Affichage des entités nommées détectées
            st.markdown('<span style="font-weight:bold; text-decoration: underline; color:#132959;">Entités nommées détectées :</span>', unsafe_allow_html=True)
            for entity_text, entity_type in grouped_entities:
                color = entity_colors.get(entity_type, "black")
                st.markdown(f'<span style="background-color: {color}; color: black; padding: 6px; border-radius: 10px;"><strong>{entity_text} ({entity_type})</strong></span>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
