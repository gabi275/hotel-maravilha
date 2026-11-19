from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Hospede

class PermissoesTest(TestCase):
    def setUp(self):
        U = get_user_model()
        self.a = U.objects.create_user(username='a', password='senha-forte-123')
        self.b = U.objects.create_user(username='b', password='senha-forte-123')
        self.h = Hospede.objects.create(nome='Privado', cadastrado_por=self.a)

    def test_listagem_nao_expoe_hospede_de_outro_usuario(self):
        self.client.force_login(self.b)
        response = self.client.get(reverse('hospede_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Privado')

    def test_edicao_de_outro_usuario_retorna_404(self):
        self.client.force_login(self.b)
        self.assertEqual(self.client.get(reverse('hospede_update', args=[self.h.pk])).status_code, 404)

    def test_usuario_comum_nao_edita_quarto(self):
        self.client.force_login(self.b)
        self.assertEqual(self.client.get(reverse('quarto_create')).status_code, 403)

    def test_usuario_pode_cadastrar_hospede(self):
        self.client.force_login(self.b)
        response = self.client.post(reverse('hospede_create'), {'nome': 'Novo', 'cpf': '', 'telefone': '', 'email': ''})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Hospede.objects.filter(nome='Novo', cadastrado_por=self.b).exists())
