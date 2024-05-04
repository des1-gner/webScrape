import xml.etree.ElementTree as ET
import openpyxl

def process_xml(file_path, output_file):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Create a new workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Write the header row
    sheet.cell(row=1, column=1, value="Title")
    sheet.cell(row=1, column=2, value="Content")

    # Initialize the row counter
    row_num = 2

    # Iterate over each <item> element
    for item in root.findall('./channel/item'):
        # Extract the desired tags
        title = item.find('title').text if item.find('title') is not None else ""
        encoded_excerpt = item.find('ns3:encoded', {'ns3': 'http://wordpress.org/export/1.2/excerpt/'})

        # Check if the <ns3:encoded> tag exists and has text content
        if encoded_excerpt is not None and encoded_excerpt.text is not None:
            # Remove the <excerpt:encoded> and </excerpt:encoded> tags from the content
            content = encoded_excerpt.text.replace('<excerpt:encoded>', '').replace('</excerpt:encoded>', '')
        else:
            content = ""

        # Write the extracted data to the sheet
        sheet.cell(row=row_num, column=1, value=title)
        sheet.cell(row=row_num, column=2, value=content)

        # Increment the row counter
        row_num += 1

    # Save the workbook to the output file
    workbook.save(output_file)

# Usage example
xml_file_path = 'ibuildPosts.xml'
output_file_path = 'ibuildPosts.xlsx'
process_xml(xml_file_path, output_file_path)