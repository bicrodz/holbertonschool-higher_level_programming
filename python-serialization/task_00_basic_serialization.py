#!/usr/bin/env python3
"""Module that serializes and deserializes a dictionary using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to a JSON file, replacing it if it exists."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load a JSON file and return the dictionary it contains."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
