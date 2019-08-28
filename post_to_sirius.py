import gzip
import os
import json
import requests
import time
import argparse
import xml.etree.ElementTree as ET


class SetPoster:
    base_url = ''
    username = ''
    password = ''
    session = ''
    set_xml_file_path = ''

    def __init__(self):
        self.base_url = os.getenv('BASE_URL')
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')
        # self.set_xml_file_path = os.path.relpath(
        #     "../opg-core-ingestion-data")+"/"+set_xml_file
        self.session = requests.Session()

        auth = self.session.post(self.base_url + '/auth/login',
                                 data={
                                     'email': self.username,
                                     'password': self.password
                                 }
                                 )

        print("Auth returned {}".format(auth.status_code))

    def iterate_over_files(self):
        with open("set_files_list") as file:
            for line in file:
                set_xml_filename = line.rstrip()
                self.set_xml_file_path = os.path.relpath(
                    "../opg-core-ingestion-data")+"/"+set_xml_filename
                self.parse_xml()
                # self.post_set_file()

    def parse_xml(self):
        f = gzip.open(self.set_xml_file_path, 'rb')
        set_xml = f.read()
        set = ET.fromstring(set_xml)
        for child in set:
            print(child.tag, child.attrib)
        f.close()

    def post_set_file(self):
        f = gzip.open(self.set_xml_file_path, 'rb')
        set_xml = f.read()
        post = self.session.post(self.base_url + '/api/ddc',
                                 headers={'Content-Type': 'text/xml'},
                                 data=str(set_xml))
        f.close()
        print(post.status_code)
        print(post.text)


def main():
    parser = argparse.ArgumentParser(
        description="Look up LPA IDs on the Sirius API Gateway.")

    # parser.add_argument("set_xml_file", type=str,
    #                     help="LPA ID to look up in API Gateway")

    args = parser.parse_args()
    work = SetPoster()
    work.iterate_over_files()


if __name__ == "__main__":
    main()
