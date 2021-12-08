#!/usr/bin/env python3
"""Adv. task 14 Top students
"""
import pymongo


def top_students(mongo_collection):
    """Returns all students sorted by average score
    The top must be ordered
    Average score must be part of each item returns with key = averageScore
    """
    return mongo_collection.aggregate([
        {
            '$project':
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
