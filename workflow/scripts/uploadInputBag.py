import argparse
from deriva.core import ErmrestCatalog, get_credential, BaseCLI
import sys
import csv
from datetime import datetime

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="file", required=True)
    parser.add_argument('-l', '--loc', help="location", required=True)
    parser.add_argument('-s', '--md5', help="md5", required=True)
    parser.add_argument('-b', '--bytes', help="bytes", required=True)
    parser.add_argument('-o', '--host', help="bytes", required=True)
    parser.add_argument('-c', '--cookie', help="bytes", required=True)
    args = parser.parse_args()
    return args

def main(hostname, catalog_number, credential):
    catalog = ErmrestCatalog('https', hostname, catalog_number, credential)
    pb = catalog.getPathBuilder()
    inputBag_table = pb.RNASeq.Input_Bag

    inputBag_data = {
        "File_Name": args.file,
        "File_URL": args.loc,
        "File_MD5": args.md5,
        "File_Bytes": args.bytes,
        "File_Creation_Time": datetime.now().replace(microsecond=0).isoformat(),
        "Notes": "TEST",
        "Bag_Type": "Replicate_Input_Seq"
        }

    entities = inputBag_table.insert([inputBag_data])
    rid = entities[0]["RID"]

    print(rid)
    
        
if __name__ == '__main__':
    args = get_args()
    cli = BaseCLI("Custom RNASeq query", None, 1)
    cli.remove_options(["--config-file"])
    host = args.host
    credential = {"cookie": args.cookie}
    main(host, 2, credential)