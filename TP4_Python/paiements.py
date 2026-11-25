
from abc import ABC, abstractmethod


class Paiement(ABC):
    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)

        if not self.verifier_numero(numero):
            raise ValueError("Numéro de carte invalide.")

        if not cvv.isdigit() or len(cvv) not in (3, 4):
            raise ValueError("CVV invalide.")

        self.numero = numero
        self.cvv = cvv

    @staticmethod
    def verifier_numero(numero):
        if not numero.isdigit():
            return False

        chiffres = [int(c) for c in numero]
        chiffres.reverse()

        total = 0

        for i, chiffre in enumerate(chiffres):
            if i % 2 == 1:
                chiffre *= 2
                if chiffre > 9:
                    chiffre -= 9
            total += chiffre

        return total % 10 == 0

    def payer(self):
        return f"Paiement de {self._montant}€ par Carte Bancaire confirmé."


class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)

        if "@" not in email or "." not in email:
            raise ValueError("Email invalide.")

        if not token:
            raise ValueError("Token API obligatoire.")

        self.email = email
        self.token = token

    def payer(self):
        return f"Paiement de {self._montant}€ par PayPal confirmé."


class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)

        if not wallet_id:
            raise ValueError("Wallet ID obligatoire.")

        if reseau not in ("BTC", "ETH"):
            raise ValueError("Réseau non reconnu.")

        self.wallet_id = wallet_id
        self.reseau = reseau

    def payer(self):
        return (
            f"Paiement de {self._montant}€ "
            f"par Crypto ({self.reseau}) confirmé."
        )


def traiter_paiements(liste):
    for paiement in liste:
        print(paiement.payer())


if __name__ == "__main__":

    paiements = [
        CarteBancaire(200, "4532015112830366", "123"),
        CarteBancaire(350, "4111111111111111", "456"),

        PayPal(150, "alice@gmail.com", "TOKEN123"),
        PayPal(250, "bob@gmail.com", "TOKEN456"),

        Crypto(500, "WALLET001", "BTC"),
        Crypto(700, "WALLET002", "ETH")
    ]

    traiter_paiements(paiements)
