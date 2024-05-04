import xml.etree.ElementTree as ET

def remove_metadata(file_path, output_file):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Remove <wp:author> tags and their contents
    for author in root.findall('./channel/wp:author', {'wp': 'http://wordpress.org/export/1.2/'}):
        root.find('./channel').remove(author)

    # Remove <wp:tag> and <wp:category> tags and their contents
    for item in root.findall('./channel/item'):
        for tag in item.findall('./category'):
            item.remove(tag)

    # Remove <wp:postmeta> tags and their contents
    for item in root.findall('./channel/item'):
        for postmeta in item.findall('./wp:postmeta', {'wp': 'http://wordpress.org/export/1.2/'}):
            item.remove(postmeta)

    # Remove <wp:commentmeta> tags and their contents
    for item in root.findall('./channel/item'):
        for comment in item.findall('./wp:comment', {'wp': 'http://wordpress.org/export/1.2/'}):
            for commentmeta in comment.findall('./wp:commentmeta', {'wp': 'http://wordpress.org/export/1.2/'}):
                comment.remove(commentmeta)

    # Remove <wp:termmeta> tags and their contents
    for term in root.findall('./channel/wp:term', {'wp': 'http://wordpress.org/export/1.2/'}):
        for termmeta in term.findall('./wp:termmeta', {'wp': 'http://wordpress.org/export/1.2/'}):
            term.remove(termmeta)

    # Remove <wp:meta> tags and their contents
    for meta in root.findall('./channel/wp:meta', {'wp': 'http://wordpress.org/export/1.2/'}):
        root.find('./channel').remove(meta)

    # Save the modified XML to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Usage example
xml_file_path = 'ibuildPosts.xml'
output_file_path = 'ibuildPosts_cleaned.xml'
remove_metadata(xml_file_path, output_file_path)