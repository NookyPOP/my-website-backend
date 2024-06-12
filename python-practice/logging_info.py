import sys

import logging

import json

# print(sys.modules.get("logging_info"))


from io import StringIO

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(filename="myapp.log", level=logging.INFO)
    logger.info("Started")
    print("Hello World!")
    logger.info("Finished")
    obj = {"name": "Bougnazal", "first_names": ["Emile", "Raoul"]}
    encode_json = json.dumps(obj)
    print(encode_json, type(encode_json), obj)
    decode_json = json.loads(encode_json)
    print(decode_json, type(decode_json))
    list_of_objects = [{"name": "Bougnazal", "first_names": ["Emile", "Raoul"]}, "jack"]
    print(json.dumps(list_of_objects))
    print(json.dumps("\\dir\bile.text"))
    ios = StringIO()
    json.dump(["hello", "world"], ios)
    encode_dump = ios.getvalue()
    print(encode_dump, type(encode_dump))
    iox = StringIO(encode_dump)
    i0_decoded = json.load(iox)
    print(i0_decoded, type(i0_decoded))


if __name__ == "__main__":
    main()
