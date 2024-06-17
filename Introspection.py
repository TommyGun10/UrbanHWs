from pprint import pprint
import inspect


def introspection_info(obj):
    return (f"Type of object: {type(obj)}", f"Attributes and Methods of object: {dir(obj)}",
            f"Module of object: {inspect.getmodule(obj)}")

pprint(introspection_info(25.10))
