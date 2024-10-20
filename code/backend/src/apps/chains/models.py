from django.db import models

from apps.common.models import AbstractBaseModel


class Chain(AbstractBaseModel):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=32)
    chain_id = models.PositiveBigIntegerField(unique=True)
    network_id = models.PositiveBigIntegerField()
    info_url = models.URLField(max_length=2048)

    gecko_id = models.CharField(max_length=255)
    gecko_logo_thumb_url = models.URLField(max_length=2048, null=True)
    gecko_logo_small_url = models.URLField(max_length=2048, null=True)
    gecko_logo_large_url = models.URLField(max_length=2048, null=True)

    def __str__(self):
        return (
            f"{self.name} ({self.short_name}) | "
            f"Chain ID: {self.chain_id} | "
            f"Network ID: {self.network_id} | "
            f"{'Enabled' if not self.deleted_at else 'Disabled'}"
        )


class ChainRPC(AbstractBaseModel):
    chain = models.ForeignKey('apps.Chain', related_name='rpcs_rel', on_delete=models.CASCADE)
    url = models.URLField(max_length=2048, unique=True)

    weight = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('-deleted_at', '-weight',)

    def __str__(self):
        return (
            f"{self.chain.name} | "
            f"{self.url} | "
            f"{'Enabled' if not self.deleted_at else 'Disabled'}"
        )


class Token(AbstractBaseModel):
    chain = models.ForeignKey('apps.Chain', related_name='tokens_rel', on_delete=models.CASCADE)
    is_native = models.BooleanField(default=False)
    address = models.CharField(max_length=128, null=True)  # native tokens don't have an address
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=32)
    decimals = models.PositiveSmallIntegerField(default=18)
    logo_uri = models.URLField(max_length=2048, null=True)

    class Meta:
        unique_together = (
            ('chain', 'address'),
        )

    def __str__(self):
        return (
            f"{self.name} ({self.symbol}) | "
            f"Chain: {self.chain.name} | "
            f"{'Native' if self.is_native else 'Not native'} | "
            f"{'Enabled' if not self.deleted_at else 'Disabled'}"
        )
