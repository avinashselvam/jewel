import spacy
from openai import OpenAI
from utils import get_component_and_attributes, rank_tags
import os
import streamlit as st
from attributes import ALL_ATTRIBUTES

def main(nlp):

    st.title("Tag ranker")

    secret_key = st.text_input("open ai key")

    if secret_key:

        os.environ['OPENAI_API_KEY'] = secret_key
        openai_client = OpenAI()

    input_text = st.text_input("Describe your ornament")

    if st.button("Search Tags"):

        component_and_attributes = get_component_and_attributes(openai_client, input_text)

        for component, attributes in component_and_attributes.items():

            st.text(f'For {component}')

            for attr_key, attr_value in attributes.items():

                st.text(f'identified {attr_key}: {attr_value}')

                ranked_tags = rank_tags(nlp, attr_value, ALL_ATTRIBUTES[attr_key])
                ranked_tags_str = ", ".join([f'{tag}: {score:.2f}' for (tag, score) in ranked_tags])
                st.text(f'ranked {ranked_tags_str}')

if __name__ == "__main__":

    nlp = spacy.load('en_core_web_lg')
    main(nlp)
