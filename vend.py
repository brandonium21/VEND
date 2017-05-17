import gspread

credentials = {
  "type": "service_account",
  "project_id": "fabvend-167916",
  "private_key_id": "3a6ea4486f9a9dd2bb7c7cddd53b756e5e3074ba",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC8vEIekv2LQxwa\nF3193Yl+WURZEwpto+b/VEfRyLQtoxNF8iTuurmfLI/o+FAxnjUp9VHJhCDk79fa\npCV2oXMAu0MOoidLUyiep1rHIGjx6DXww+cgxQyMswwDCKzGnbjo4BRk49n69oKy\nSx7yuWBSMCt9t4yog6ZzORGie1+At34tPWTGc5YGxNOc/8cOjeJ+B4ggC5lzh0Nm\nIEzauBW4/QZ6/yMfZSR8oy3T4t7OUFUVTahZX+L4rKbl18u+j3w0eL0Yk/wDz/Ol\n8ZiGCuBkWc6Ppd9Mgh4NlgirCH9dR7Y+5FdsJEENqOQgzlcf3LPVcwFU19muavEa\n95f+PEgNAgMBAAECggEAAdltuRijSl41zshPJFDA5vo0nL4pL9TXenCsJCaYJAsB\nMSzDvDZxLi7vbrl207L4qLjCJzwtCavoog2nXlJhAESqzgsRtn+8mf1gJYEFoOUv\nw3RaoJa9s5KSOg9iM1oFSfw0HEmimlPDCRXfr5eDFZsU5K5L6bTMiJF/wOdTkr0f\n4Dnq5zYe1fFTb2lRO4E7XGDXwEMjn0TdeILC3MS/pLWdC6us9//oMQdBqexW4Ql6\n/Pedwvfha3nI1Ng2FzbTs/x+WuxfMn5vAmWd8uGrLqPIHKjNV9Ovnp/qbqEhHWL/\nlYCJjDYEjx66f8vRr5GFiKuzmPggy4y5ZNHEAtfWQQKBgQD3F8x75+i90zSuv0em\nVQNAnO4xBqgmWokwQLVqQ+TOxHEVMmCT8bso3sHl1kD/NQRH2yDRSwbtb5Yb2sLY\nah8AJS/2qyYYLwvzHlesy3tozi79C9Q4OPMBrGCk1EyCvnTgE0tcFMh3wvPq8+Ih\nN16NnZlr1nBQsOHhImFyaP4l7QKBgQDDie3mwhiLxKx/Mt0DGKJF0EZFDTT8iSa1\nPzzCOF4K6J4cwZaH3ci8UtJSWbgk0F3qGbXAbqGf4gnc+x5pOilKxJeBXHZpssMB\nD/Ss4B6fqS8abMxFFwCdWibRDQ8kFJRknwZkOF7eKoA8zaa4PsjJ/J95MBzQzzfC\nnZBvFzJmoQKBgFkYdLws2AgycumbwSshtkWDEIQPAWyq8pK6km+ZwZQo0xmwi5Bs\n9m57O/Ey+0bKiBuc0M2Gvx24QakTjXRZd4om3o+UEO1hcW6df0GoMXyN8/V8YW5Q\nYpc037gvcNMn956gdmjieZJtcmRCwkP14hswO5Tdwqvly9zQ99A4OYPVAoGBAId2\nlIOaz5p0g/QS7p3ogPLQmP3Zam3RLim+R39dwXjZMkBFtN0nPpuI3QAD+9g1Kfq2\nGP3ZJss2sxKOPcE0c8rCaxtJTRdoqkOgJCdnlI+Ti3hJCzKJ/vkDrYSCAY1DXJJg\nwPLJQp+y3ehBqFBX3o5gHrK8LBpUlBKVSaxMa7RBAoGAEk7enGT55jVuynUAAlMv\nW387YAJrfvxOo/AwofwUp9WQTMRmZKLsGrGCwdRtK5tVC3wa2j3qmawFFC/jMEpY\ns8U9ASaBNQ5lmI8E45ac2yonMaSIM2kZpR+dc9IZ8GOqc9Ni9Cr0UIifeI4/vMdf\nK/uyX9op731lQtImsQ4vocI=\n-----END PRIVATE KEY-----\n",
  "client_email": "vend-database@fabvend-167916.iam.gserviceaccount.com",
  "client_id": "102646852049206070934",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vend-database%40fabvend-167916.iam.gserviceaccount.com"
}

gc = gspread.authorize(credentials)

# Open a worksheet from spreadsheet with one shot
wks = gc.open("Fab_VEND_database").sheet1

def add_funds(wallet_code, amt):
    consumer = wks.find(str(wallet_code))
    print consumer
    pass

def remove_funds(wallet_code, amt):
    pass

def get_funds(wallet_code):
    pass

def get_info(wallet_code):
    pass

add_funds('8h63gd9')
