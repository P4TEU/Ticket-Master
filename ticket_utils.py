import discord
from discord import PermissionOverwrite
from config import TICKET_CATEGORY_NAME, TICKET_PREFIX, SUPPORT_ROLE_ID


async def create_ticket_channel(guild: discord.Guild, user: discord.Member, client) -> discord.TextChannel:
# găsește/creează categoria
category = discord.utils.get(guild.categories, name=TICKET_CATEGORY_NAME)
if not category:
category = await guild.create_category(TICKET_CATEGORY_NAME)


safe_name = f"{TICKET_PREFIX}{user.name.lower().replace(' ', '-')}-{user.discriminator}"


overwrites = {
guild.default_role: PermissionOverwrite(view_channel=False),
user: PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
}


if SUPPORT_ROLE_ID:
role = guild.get_role(SUPPORT_ROLE_ID)
if role:
overwrites[role] = PermissionOverwrite(view_channel=True, send_messages=True)


channel = await guild.create_text_channel(name=safe_name, category=category, overwrites=overwrites, topic=f'Ticket pentru {user}')" + "
" + "# Trimite aici detalii despre problema ta"


# mesaj initial cu buton de close
view = discord.ui.View()
view.add_item(discord.ui.Button(label='Închide ticket', style=discord.ButtonStyle.danger, custom_id='close_ticket'))
await channel.send(f'{user.mention} Mulțumim — un membru al staff va veni în curând. Apasă butonul pentru a închide ticketul.', view=view)


return channel


async def close_ticket_channel(channel: discord.TextChannel, user: discord.Member, client):
# opțiuni: arhivare -> salvare transcript -> delete
try:
await channel.delete(reason=f'Ticket închis de {user}')
except Exception as e:
print('Eroare la închidere ticket:', e)
