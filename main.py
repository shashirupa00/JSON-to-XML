import json
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import argparse

def json_to_xml(json_data):
    def _json_to_xml_recurse(data, parent=None):
        #Recursively convert JSON data to XML elements.
        if isinstance(data, dict):
            # Handle JSON objects
            elem = ET.Element('object')
            for key, value in data.items():
                child = _json_to_xml_recurse(value)
                child.set("name", key)
                elem.append(child)
        
        elif isinstance(data, list):
            # Handle JSON arrays
            elem = ET.Element('array')
            for item in data:
                elem.append(_json_to_xml_recurse(item))
        
        elif isinstance(data, bool):
            # Handle boolean values
            elem = ET.Element("boolean")
            elem.text = str(data).lower()
        
        elif isinstance(data, (int, float)):
            # Handle numeric values
            elem = ET.Element("number")
            elem.text = str(data)
        
        elif isinstance(data, str):
            # Handle string values
            elem = ET.Element("string")
            elem.text = data
        
        elif data is None:
            # Handle null values
            elem = ET.Element("null")
        
        else:
            raise ValueError(f"Unsupported type: {type(data)}")
        
        return elem
    
    return _json_to_xml_recurse(json_data)

def pretty_print_xml(element):
    #Convert XML element to a pretty-printed string.

    rough_string = ET.tostring(element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def main():
    # Set up command-line argument parser

    parser = argparse.ArgumentParser(description="JSON to XML conversion")
    parser.add_argument("input_file", help="Path to your input file")
    parser.add_argument("output_file", help="Path to you output file")
    args = parser.parse_args()

    try:
        # Read and parse JSON input file
        with open(args.input_file, 'r') as f:
            json_data = json.load(f)
        
        # Convert JSON to XML
        xml_root = json_to_xml(json_data)
        # Pretty print the XML
        pretty_xml = pretty_print_xml(xml_root)

        # Write the XML to the output file
        with open(args.output_file, 'w') as f:
            f.write(pretty_xml)

        print(f"Successfully converted {args.input_file} to {args.output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
if __name__ == "__main__":
    main()

