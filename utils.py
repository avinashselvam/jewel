import ast

def get_component_and_attributes(client, jewellery_description):

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You're a smart and intelligent entity recognition system. You're given a task of idenitifying different jewellery components and their attributes\
                        COMPONENT: components of an ornament such as pendant, link\
                        ATTRIBUTE: descriptive words about the components - shape, color, size, stone, style, metal\
                        Output Format\
                        {'COMPONENT1': {'shape': 'shape of component', 'color': 'color of component'}, 'COMPONENT2': {'shape': 'shape of component', 'style': 'style of the component'}}\
                        Example:\
                        Input: antique style chain with a large bird pendant having blue stones and flower shaped chain links\
                        Output: {'pendant': {'shape': 'bird', 'color': 'blue', 'size': 'large', 'style': 'antique'}, 'chain link': {'shape': 'flower'}}"
             },
            {"role": "user",
             "content": f"Input: {jewellery_description}\
                        Output:"
            }
        ]
    )

    return ast.literal_eval(completion.choices[0].message.content)

def rank_tags(nlp, query, tags):

    """
    Args
        nlp: spacy nlp object
        query: the word for which we need to rank the tags for
        tags: list of tags
    Returns
        list of (tag, similarity score) for each tag in that category
    """

    scored_and_sorted_tags = sorted([(tag, nlp(tag).similarity(nlp(query))) for tag in tags], key=lambda x: -x[1])

    return scored_and_sorted_tags