from ansible.module_utils.basic import *
import re
import requests
import psutil
import json
import subprocess

def check_process(user, process):
    for proc in psutil.process_iter(attrs=['name', 'username']):
        if proc.info['name'] == process:
            if proc.info['username'] == user:
                print(json.dumps({"Process running under correct user": process}))


def check_port(process):
    data = dict()
    for proc in psutil.process_iter(attrs=['name', 'pid']):
        if proc.info["name"] == process:
            process_id = psutil.Process(proc.info['pid'])
            for con in process_id.connections("tcp6"):
                if con.status == "LISTEN":
                    data["port"] = con.laddr[1]
            print(json.dumps(data))


def check_url_content(url, regex_str):
    r = requests.get(url)
    s = r.content
    result = re.findall(regex_str, s)
    print(json.dumps({
        'content': {
            'responce_code': r.status_code,
            'contains': result
        },
    }))


def check_url_headers_server(url, regex_str_srv):
    p = subprocess.Popen(["curl", "-ILs", url], stdout=subprocess.PIPE)
    match = re.findall(re.template(regex_str_srv), str(p.communicate()[0]))
    print(json.dumps({
        'header': match
    }))

module = AnsibleModule(
    argument_spec={'process': {'required': False, 'type': str, 'Default': None},
                   'user': {'required': False, 'type': str, 'Default': None},
                   'url': {'required': False, 'type': str, 'default': None},
                   'regex_str': {'required': False, 'type': str, 'default': None},
                   'regex_str_srv': {'required': False, 'types': str, 'default': None}}
)

if module.params['user'] != None and module.params['process'] != None:
    check_process(module.params['user'], module.params['process'])
if module.params['process'] != None and module.params['user'] == None:
    check_port(module.params['process'])
if module.params['url'] != None and module.params['regex_str'] != None:
    check_url_content(module.params['url'], module.params['regex_str'])
if module.params['url'] != None and module.params['regex_str_srv'] != None:
    check_url_headers_server(module.params['url'], module.params['regex_str_srv'])