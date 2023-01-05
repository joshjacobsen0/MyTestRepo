from ncclient import manager

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

with manager.connect(
    host=router["host"],
    port=router["port"],
    username=router["username"],
    password=router["password"],
    hostkey_verify=False
) as m:
    m.close_session()
