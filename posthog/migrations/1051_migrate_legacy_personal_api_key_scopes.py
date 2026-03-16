from django.db import migrations


def migrate_legacy_scopes(apps, schema_editor):
    PersonalAPIKey = apps.get_model("posthog", "PersonalAPIKey")
    PersonalAPIKey.objects.filter(scopes__isnull=True).update(scopes=["*"])


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "1050_rename_slack_twig_to_posthog_code"),
    ]

    operations = [
        migrations.RunPython(migrate_legacy_scopes, migrations.RunPython.noop, elidable=True),
    ]
