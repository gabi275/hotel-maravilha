from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class ConvidadoPermissoesTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='convidado', password='senha-teste-123')
        self.client.force_login(self.user)
    def test_nao_pode_cadastrar(self):
        for url in ('hospede_create', 'reserva_create', 'hospedagem_create', 'quarto_create'):
            with self.subTest(url=url):
                self.assertEqual(self.client.get(reverse(url)).status_code, 403)
                self.assertEqual(self.client.post(reverse(url), {}).status_code, 403)
    def test_pode_consultar(self):
        self.assertEqual(self.client.get(reverse('pagina_inicial')).status_code, 200)
        self.assertEqual(self.client.get(reverse('reserva_list')).status_code, 200)
