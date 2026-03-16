import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "1050_rename_slack_twig_to_posthog_code"),
        ("error_tracking", "0012_suppression_rule_bytecode_and_sampling_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="errortrackingspikedetectionconfig",
            name="recently_spiking_hours",
            field=models.IntegerField(default=4),
        ),
        migrations.CreateModel(
            name="ErrorTrackingSpikeEvent",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ("issue_id", models.UUIDField()),
                ("detected_at", models.DateTimeField()),
                ("computed_baseline", models.FloatField()),
                ("current_bucket_value", models.IntegerField()),
                ("issue_name", models.TextField(blank=True, null=True)),
                ("issue_description", models.TextField(blank=True, null=True)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posthog.team",
                    ),
                ),
            ],
            options={
                "db_table": "posthog_errortrackingspikeevent",
                "indexes": [
                    models.Index(fields=["team", "-detected_at"], name="posthog_err_team_id_e37c4c_idx"),
                    models.Index(fields=["issue_id", "-detected_at"], name="posthog_err_issue_i_38a8b0_idx"),
                ],
            },
        ),
    ]
