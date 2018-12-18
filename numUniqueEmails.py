def numUniqueEmails(emails):
    return len(set(map(lambda x: x[0] + x[1], map(lambda name: [name[0][:(name[0].find('+') if name[0].find('+') != -1 else len(name[0]))].replace('.', ''), name[1]], map(lambda email: email.split('@'), emails)))))
