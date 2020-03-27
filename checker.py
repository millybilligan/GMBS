def checkPort(port):
    if port == 1:
        return 'Supposed service : tcpmux'
    if port == 7:
        return 'Supposed service : echo'
    if port == 11:
        return 'Supposed service : systat'
    if port == 13:
        return 'Supposed service : daytime'
    if port == 17:
        return 'Supposed service : qotd'
    if port == 18:
        return 'Supposed service : msp'
    if port == 19:
        return 'Supposed service : chargen'
    if port == 20:
        return 'Supposed service : ftp-data'
    if port == 21:
        return 'Supposed service : ftp'
    if port == 22:
        return 'Supposed service : ssh'
    if port == 23:
        return 'Supposed service : telnet'
    if port == 24:
        return 'Supposed service : private port!'
    if port == 25:
        return 'Supposed service : smtp'
    if port == 37:
        return 'Supposed service : time'
    if port == 42:
        return 'Supposed service : nameserver'
    if port == 43:
        return 'Supposed service : whois'
    if port == 49:
        return 'Supposed service : tacacs'
    if port == 53:
        return 'Supposed service : domain'
    if port == 57:
        return 'Supposed service : mtp'
    if port == 67:
        return 'Supposed service : bootps'
    if port == 68:
        return 'Supposed service : bootpc'
    if port == 70:
        return 'Supposed service : gopher'
    if port == 77:
        return 'Supposed service : rje'
    if port == 79:
        return 'Supposed service : finger'
    if port == 80:
        return 'Supposed service : www'
    if port == 87:
        return 'Supposed service : link'
    if port == 88:
        return 'Supposed service : kerberos-sec'
    if port == 95:
        return 'Supposed service : supdup'
    if port == 101:
        return 'Supposed service : hostname'
    if port == 102:
        return 'Supposed service : iso-tsap'
    if port == 104:
        return 'Supposed service : acr-nema'
    if port == 110:
        return 'Supposed service : pop3'
    if port == 111:
        return 'Supposed service : sunrpc'
    if port == 113:
        return 'Supposed service : auth'
    if port == 115:
        return 'Supposed service : sftp'
    if port == 119:
        return 'Supposed service : nntp'
    if port == 135:
        return 'Supposed service : epmap'
    if port == 137:
        return 'Supposed service : netbios-ns'