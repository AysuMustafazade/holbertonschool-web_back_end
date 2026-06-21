#!/usr/bin/env python3
"""Inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""
    return mongo_collection.insert(kwargs).inserted_id
