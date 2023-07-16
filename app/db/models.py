from tortoise import fields, models
# from tortoise.contrib.pydantic import pydantic_model_creator


class Rate(models.Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    cargo_type = fields.CharField(max_length=100)
    rate = fields.FloatField()

    def __str__(self) -> str:
        return self.cargo_type


# User_Pydantic = pydantic_model_creator(Rate, name="Rate")
