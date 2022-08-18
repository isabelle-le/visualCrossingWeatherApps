import sys, os
import requests as req
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.modularinput import *


class MyScript(Script):

    def get_scheme(self):
        # Returns scheme.
        scheme = Scheme("Visual Crossing Weather")
        scheme.use_external_validation = False
        scheme.use_single_instance = False
        scheme.description = "TMDB Modular Input"

        api_key = Argument("api_key")
        api_key.title = "API Key"
        api_key.data_type = Argument.data_type_string
        api_key.description = "API Key"
        api_key.required_on_create = True
        api_key.required_on_edit = True
        scheme.add_argument(api_key)

        lang = Argument("unitGroup")
        lang.title = "Unit Group "
        lang.data_type = Argument.data_type_string
        lang.description = "Unit Type"
        lang.required_on_create = False
        lang.required_on_edit = False
        scheme.add_argument(lang)

        page_number = Argument("location")
        page_number.title = "Location"
        page_number.data_type = Argument.data_type_number
        page_number.description = "Location"
        page_number.required_on_create = False
        page_number.required_on_edit = False
        scheme.add_argument(page_number)

        region = Argument("contentType")
        region.title = "Content Type"
        region.data_type = Argument.data_type_string
        region.description = "Content Type"
        region.required_on_create = False
        region.required_on_edit = False
        scheme.add_argument(region)

        return scheme


    def validate_input(self, validation_definition):
        # Validates input.
        pass

    def stream_events(self, inputs, ew):
        pass
        # Splunk Enterprise calls the modular input,
        # streams XML describing the inputs to stdin,
        # and waits for XML on stdout describing events.
        # {"input_stanza1" : {"api_key": value, "lang": value...},"input_stanza2" : {"api_key": value, "lang": value...}}



if __name__ == "__main__":
    sys.exit(MyScript().run(sys.argv))