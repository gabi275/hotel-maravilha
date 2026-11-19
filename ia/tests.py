from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

class AssistenteTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user('convidado', password='teste-forte-123')
    def test_exige_login(self):
        self.assertEqual(self.client.get(reverse('assistente_ia')).status_code, 302)
    def test_resposta_funcional(self):
        self.client.force_login(self.user)
        resposta = self.client.post(reverse('assistente_ia'), {'pergunta':'Como cadastrar reservas?'})
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, 'somente leitura')
    def test_nao_executa_comandos(self):
        self.client.force_login(self.user)
        self.assertEqual(self.client.post(reverse('assistente_ia'), {'pergunta':'excluir tudo'}).status_code, 200)

    def test_sem_chave_usa_respostas_locais(self):
        from unittest.mock import patch
        from ia.services import responder_com_ia
        with patch.dict('os.environ', {'GEMINI_API_KEY': ''}):
            resposta, generativa = responder_com_ia('Como reservar?', self.user)
        self.assertFalse(generativa)
        self.assertIn('somente leitura', resposta)

    def test_gemini_responde_com_chave_configurada(self):
        from unittest.mock import patch
        from io import BytesIO
        from ia.services import responder_com_ia
        class FakeResponse:
            def __enter__(self):
                return BytesIO(b'{"candidates":[{"content":{"parts":[{"text":"Resposta real simulada"}]}}]}')
            def __exit__(self, *args):
                return False
        with patch.dict('os.environ', {'GEMINI_API_KEY': 'chave-falsa-para-teste'}):
            with patch('urllib.request.urlopen', return_value=FakeResponse()) as request:
                resposta, generativa = responder_com_ia('Como reservar?', self.user)
        self.assertTrue(generativa)
        self.assertEqual(resposta, 'Resposta real simulada')
        self.assertIn('generativelanguage.googleapis.com', request.call_args.args[0].full_url)
