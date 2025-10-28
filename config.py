from os import getenv

TOKEN = getenv('DISCORD_TOKEN')
GUILD_ID = int(getenv('GUILD_ID')) if getenv('GUILD_ID') else None
SUPPORT_ROLE_ID = int(getenv('SUPPORT_ROLE_ID')) if getenv('SUPPORT_ROLE_ID') else None
TICKET_CATEGORY_NAME = getenv('TICKET_CATEGORY_NAME', 'Tickets')
TICKET_PREFIX = 'ticket-'
