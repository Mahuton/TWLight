# Generated by Django 3.0.11 on 2020-11-20 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0066_move_editcounts_to_log"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="editor",
            name="wp_editcount",
        ),
        migrations.RemoveField(
            model_name="editor",
            name="wp_editcount_prev",
        ),
        migrations.RemoveField(
            model_name="editor",
            name="wp_editcount_prev_updated",
        ),
        migrations.RemoveField(
            model_name="editor",
            name="wp_editcount_updated",
        ),
    ]
