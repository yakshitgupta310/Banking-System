from Client import Client


class Bank:
    Name = "ABC Bank"
    clients = []

    def update_db(self, client):
        self.clients.append(client)

    def authentication(self, name, account_no):
        for i in range(len(self.clients)):
            if (name in self.clients[i].account.values()) and (account_no in self.clients[i].account.values()):
                # print("Authentication Succesfull !")
                # print(self.clients[i].account)
                self.user = self.clients[i]
                return(self.user)
            # print("No match found!!")
