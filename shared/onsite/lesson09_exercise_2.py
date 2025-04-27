def projdi_vsechny_udaje(*emaily):
    jmena = set()

    for email in emaily:
        if "end" in email:
            break
        jmeno, domena = rozdel_email(email)
        jmena.add(jmeno)
    
    return jmena


def rozdel_email(email):
    return email.split("@")


projdi_vsechny_udaje(
    'petra.fulinova@firma.cz',  # 'petra.fulinova', 'firma.cz'
    'adela.vancurova@firma.cz',
    'andrea.hertlova@firma.cz',
    'petr.vyhnis@firma.cz',
    'jan.feckanin@firma.cz',
    'pavel.harant@firma.cz',
    'zdenka.bendova@firma.cz',
    'monika.miczova@firma.cz',
    'jan.mosquito@firma.cz',
    'barbora.suvova@firma.cz',
    'lenka.kafkova@firma.cz',
    'nikola.hoffmannova@firma.cz',
    'daniela.sedlakova@firma.cz',
    'ivana.jerabkova@firma.cz',
    'valeria.jagerska@firma.cz',
    'hana.bayerova@firma.cz',
    'tomas.zamecnik@firma.cz',
    'helena.strasilova@firma.cz',
    'jana.kralova@firma.cz',
    'hermina.duskova@firma.cz',
    'dana.mirgova@firma.cz',
    'end',
    '...'
)
