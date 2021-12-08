#!/usr/bin/env python3
"""Log stats
"""
import pymongo


def count_documents(db_logs, obj={}):
    """return a logs output
    """
    return db_logs.count_documents(obj)


def log_stats():
    """provide stats about Nginx logs stored in MongoDB
    """
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    nginx_data = client.logs.nginx

    print(f"{count_documents(nginx_data)} logs")
    print("Methods:")
    for method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
        ndata = count_documents(nginx_data, {'method': method})
        print(f"\tmethod {method}: {ndata}")

    check = count_documents(nginx_data, {'method': 'GET', 'path': '/status'})
    print(f"{check} status check")


if __name__ == '__main__':
    log_stats()
