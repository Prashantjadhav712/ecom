# Generated by Django 4.2.3 on 2023-08-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerceapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=100)),
                ("catagory", models.CharField(default="", max_length=50)),
                ("subcategory", models.CharField(default="", max_length=50)),
                ("price", models.IntegerField(default=0)),
                ("desc", models.CharField(max_length=300)),
                ("image", models.ImageField(upload_to="images/images")),
            ],
        ),
    ]