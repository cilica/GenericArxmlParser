# ARXML parser Swiss Army Knife

- Parser was generated with [generateDS](https://pypi.org/project/generateDS/) (generator of python parser and exported based on xdm schema)
- Generated file (parser_autosar43.py) was altered to remove the export part (file is huge even so)
- Sample usage of the parser can be seen in parser_user.py

## Future stuff to add:

- Get the objects based on XPath. Some tools provide the xpath of a specific Xml node and you can just copy paste that into a function as a string parameter and that function should return the node at that path using the parser.