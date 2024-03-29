# Generated by Django 4.1.6 on 2023-02-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'животное',
                'verbose_name_plural': 'животные',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='AnimalKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'вид животного',
                'verbose_name_plural': 'вид животных',
                'ordering': ['name'],
            },
        ),
    ]
