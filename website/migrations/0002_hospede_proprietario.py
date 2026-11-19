from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def associar_hospedes_sem_ambiguidade(apps, schema_editor):
    Hospede = apps.get_model('website', 'Hospede')
    Reserva = apps.get_model('website', 'Reserva')
    for hospede in Hospede.objects.filter(cadastrado_por__isnull=True).iterator():
        donos = list(Reserva.objects.filter(hospede_id=hospede.pk).values_list('cadastrado_por_id', flat=True).distinct()[:2])
        if len(donos) == 1:
            hospede.cadastrado_por_id = donos[0]
            hospede.save(update_fields=['cadastrado_por'])

class Migration(migrations.Migration):
    dependencies = [('website', '0001_initial'), migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.AddField(model_name='hospede', name='cadastrado_por', field=models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT, null=True, blank=True, related_name='hospedes')),
        migrations.RunPython(associar_hospedes_sem_ambiguidade, migrations.RunPython.noop),
    ]
