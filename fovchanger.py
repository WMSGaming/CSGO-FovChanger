import pymem.process


print("""╔═╗┌─┐┬  ┬  ╔═╗┬ ┬┌─┐┌┐┌┌─┐┌─┐┬─┐  ┌┐ ┬ ┬  ╦ ╦╔╦╗╔═╗
╠╣ │ │└┐┌┘  ║  ├─┤├─┤││││ ┬├┤ ├┬┘  ├┴┐└┬┘  ║║║║║║╚═╗
╚  └─┘ └┘   ╚═╝┴ ┴┴ ┴┘└┘└─┘└─┘┴└─  └─┘ ┴   ╚╩╝╩ ╩╚═╝""")

GetFov = input('Enter fov:')

#################################
# CSGO offsets, update if needed
#################################
dwLocalPlayer = 14394812
m_iDefaultFOV = 13116
m_hViewModel = 13064
################################


pm = pymem.Pymem("csgo.exe")

client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

player = pm.read_int(client + dwLocalPlayer)


def main():
    while True:
        pm.write_int(player + m_iDefaultFOV, int(GetFov))
main()
