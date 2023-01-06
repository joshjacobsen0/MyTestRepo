from ncclient import manager
import sys
import xml.dom.minidom

sandboxURL = "sandbox-iosxe-recomm-1.cisco.com"
sandboxPort = "830"
sandboxUser = "developer"
sandboxPass = "C1sco12345"

router = {
    "host": sandboxURL,
    "port": sandboxPort,
    "username": sandboxUser,
    "password": sandboxPass
}

m = manager.connect(
    host=router["host"],
    port=router["port"],
    username=router["username"],
    password=router["password"],
    hostkey_verify=False
)

m.close_session()
