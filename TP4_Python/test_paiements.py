
import unittest

from paiements import CarteBancaire, PayPal, Crypto


class TestPaiements(unittest.TestCase):

    def test_carte_bancaire(self):
        paiement = CarteBancaire(
            200, "4532015112830366", "123"
        )
        resultat = paiement.payer()

        self.assertIn("200", resultat)
        self.assertIn("Carte Bancaire", resultat)

    def test_paypal(self):
        paiement = PayPal(
            150, "alice@gmail.com", "TOKEN123"
        )
        resultat = paiement.payer()

        self.assertIn("150", resultat)
        self.assertIn("PayPal", resultat)

    def test_crypto(self):
        paiement = Crypto(
            500, "WALLET001", "BTC"
        )
        resultat = paiement.payer()

        self.assertIn("500", resultat)
        self.assertIn("Crypto", resultat)

    def test_montant_invalide(self):
        with self.assertRaises(ValueError):
            PayPal(0, "alice@gmail.com", "TOKEN123")

    def test_carte_invalide(self):
        with self.assertRaises(ValueError):
            CarteBancaire(200, "123456", "123")


if __name__ == "__main__":
    unittest.main()
