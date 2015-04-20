def generate_concept_HTML(concept, text):
    text_1 = '''
<div class="concept">
    ''' + concept
    text_2 = '''
</div>
<div class="text">
        ''' + text
    text_3 = '''
</div>'''
    full_html_text = text_1 + text_2 + text_3
    return full_html_text

def make_HTML(p):
    concept = p[0]
    text = p[1]
    return generate_concept_HTML(concept, text)

list_of_concepts = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]


def generate_HTML_list(list_of_concepts):
    HTML = ""
    for i in list_of_concepts:
        concept = make_HTML(i)
        HTML = HTML + concept
    return HTML

print generate_HTML_list(list_of_concepts)
