from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from base.models import Account, Leak
import telegram
import asyncio
from setup.settings import TELEGRAM_BOT_TOKEN


@receiver(pre_save, sender=Account)
def update_phone_number(sender, instance, **kwargs):
    try:
        admin = Account.objects.get(name="admin")
        if instance.phone_number != admin.phone_number:
            instance.phone_number = admin.phone_number

    except Account.DoesNotExist:
        pass


@receiver(post_save, sender=Leak)
def send_message_to_channel(sender, instance, created, **kwargs):
    if created:
        async def send(msg, chat_id, token):
            bot = telegram.Bot(token=token)
            await bot.send_message(chat_id=chat_id, text=msg)

        asyncio.run(
            send(msg=f"New customer created: \n"
                     f"name: {instance.name} \n"
                     f"phone number: {instance.phone_number} \n"
                     f"account: {instance.account}",
                 chat_id="@inform_lead",
                 token=TELEGRAM_BOT_TOKEN)
        )
