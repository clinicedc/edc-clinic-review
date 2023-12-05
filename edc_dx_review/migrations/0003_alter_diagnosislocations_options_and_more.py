# Generated by Django 4.2.7 on 2023-12-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_dx_review", "0002_diagnosislocations_extra_value_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="diagnosislocations",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Diagnosis Locations",
                "verbose_name_plural": "Diagnosis Locations",
            },
        ),
        migrations.AlterModelOptions(
            name="reasonsfortesting",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Reasons for Testing",
                "verbose_name_plural": "Reasons for Testing",
            },
        ),
        migrations.RemoveIndex(
            model_name="diagnosislocations",
            name="edc_dx_revi_id_ab6550_idx",
        ),
        migrations.RemoveIndex(
            model_name="reasonsfortesting",
            name="edc_dx_revi_id_9cf36d_idx",
        ),
        migrations.AlterField(
            model_name="diagnosislocations",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="diagnosislocations",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="diagnosislocations",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AlterField(
            model_name="historicaldiagnosislocations",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="historicalreasonsfortesting",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="reasonsfortesting",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="reasonsfortesting",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="reasonsfortesting",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AddIndex(
            model_name="diagnosislocations",
            index=models.Index(fields=["name"], name="edc_dx_revi_name_a39b40_idx"),
        ),
        migrations.AddIndex(
            model_name="diagnosislocations",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_dx_revi_display_415beb_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="reasonsfortesting",
            index=models.Index(fields=["name"], name="edc_dx_revi_name_0b2844_idx"),
        ),
        migrations.AddIndex(
            model_name="reasonsfortesting",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_dx_revi_display_ee4387_idx",
            ),
        ),
    ]
