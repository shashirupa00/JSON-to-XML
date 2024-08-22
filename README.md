# JSON to XML Converter

This Python program converts JSON files to XML format according to the specified standard. It provides a simple command-line interface for easy usage.

## Project Structure

The project consists of the following files and directories:

- `main.py`: The main Python script that performs the JSON to XML conversion.
- `input_files/`: Directory containing test input JSON files. Users can add their own input files here.
- `my_output_files/`: Directory containing the XML outputs of the JSON input files.
- `output_files/`: Directory that can be used by the person using this project as a directory for their output files.

## Requirements

- Python 3.x

## Libraries Used

This project uses the following built-in Python libraries:

- `json`: For parsing JSON data (https://docs.python.org/3/library/json.html)
- `xml.etree.ElementTree`: For creating XML structures (https://docs.python.org/3/library/xml.etree.elementtree.html)
- `xml.dom.minidom`: For pretty-printing XML output (https://docs.python.org/3/library/xml.dom.minidom.html)
- `argparse`: For parsing command-line arguments (https://docs.python.org/3/library/argparse.html)

No external libraries are required.

## Building the Project

As this is a Python script, no building is required. Simply ensure you have Python 3.x installed on your system.

## Running the Program

To run the program, use the following command in your terminal:

```
python main.py <input_json_file> <output_xml_file>
```

Replace `<input_json_file>` with the path to your input JSON file, and `<output_xml_file>` with the desired path for the output XML file.

For example:

```
python main.py ./input_files/test.json ./output_files/test.xml
```

## Usage

1. Place your input JSON files in the `input_files/` directory.
2. Run the program as described above, specifying the input and output file paths.
3. The converted XML file will be created at the specified output path.

## Error Handling

The program includes basic error handling. If an error occurs during the conversion process, an error message will be displayed.

## Testing

To test the program, you can use the JSON files provided in the `input_files/` directory. The corresponding outputs can be found in the `my_output_files/` directory.

Here's an example of input and output:

### Input JSON:

```json
{
  "organization": {
    "name": "Securin",
    "type": "Inc",
    "building_number": 4,
    "floating": -17.4,
    "null_test": null
  },
  "security_related": true,
  "array_example0": ["red", "green", "blue", "black"],
  "array_example1": [1, "red", [{ "nested": true }], { "obj": false }]
}
```

### Output XML:

```xml
<?xml version="1.0" ?>
<object>
  <object name="organization">
    <string name="name">Securin</string>
    <string name="type">Inc</string>
    <number name="building_number">4</number>
    <number name="floating">-17.4</number>
    <null name="null_test"/>
  </object>
  <boolean name="security_related">true</boolean>
  <array name="array_example0">
    <string>red</string>
    <string>green</string>
    <string>blue</string>
    <string>black</string>
  </array>
  <array name="array_example1">
    <number>1</number>
    <string>red</string>
    <array>
      <object>
        <boolean name="nested">true</boolean>
      </object>
    </array>
    <object>
      <boolean name="obj">false</boolean>
    </object>
  </array>
</object>
```

This example demonstrates how the program handles various JSON data types, including nested objects, arrays, and null values.

## Notes

- The program follows the JSON to XML specification as described in the assignment.
- The program generates valid XML output with proper indentation.
